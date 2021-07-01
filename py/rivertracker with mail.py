from picamera import PiCamera, Color
import RPi.GPIO as GPIO
import time
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from datetime import datetime
import base64
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email, password
from device_config import device_id


now = datetime.now()
camera = PiCamera()
def preview():
    camera.rotation = 180

    camera.start_preview(alpha = 200)
    sleep(5)
    camera.stop_preview()

def takePic(text = "no distance aquired"):
    global now
    camera.rotation = 180
    camera.resolution = (500, 500)
    camera.start_preview()
    camera.annotate_text = "Approx. distance: ~" + text + " cm"
    camera.annotate_foreground = Color('black')
    camera.annotate_background = Color('white')
    camera.annotate_text_size = 20
    
    dt_string = now.strftime("%d %m %Y_%H:%M:%S")
    path = '/home/pi/Projects/Licenta/py/photos/%s.jpg' % dt_string
    camera.capture(path)
    camera.stop_preview()
    
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read())
    #delete pic from local storage
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The photo does not exist")
    
    return str(encoded)[2:][:-1]
    
#takePic()

def distance():
    try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print ("Waiting for sensor to settle")

      time.sleep(2)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      #print ("Distance:",distance,"cm")

    finally:
          GPIO.cleanup()
          return distance

def photoWithDistance():        
    distance_value = distance()
    print(distance_value)
    return distance_value, takePic(str(distance_value))


cred = credentials.Certificate('/home/pi/Projects/Licenta/py/river-tracker-295612-5b536a04d227.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def readDistances():
    distances_ref = db.collection(u'distances')
    docs = distances_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def addDistance(distance_value, path):
    doc_ref = db.collection(u'distances')
    doc_ref.add({
        u'distance': distance_value,
        u'photo_path': path,
        u'date_time': now.strftime("%Y-%m-%d %H:%M:%S"),
        u'device_id': device_id
    })
    
#addDistance(distance(),takePic())

#readDistances()

def dbCall():
    distance_value, path = photoWithDistance()
    check(distance_value)
    addDistance(distance_value, path)
    #readDistances()
    
def get_bounds(device_id):
    docs = db.collection(u'setup_data')
    query = docs.where(u'device_id', u'==', device_id).stream()
    low_bound = 0
    high_bound = 0
    river_height = 0
    for doc in query:
        var = doc.to_dict()
        low_bound = var['low_bound']
        high_bound = var['high_bound']
        river_height = var['river_height']
    return low_bound, high_bound, river_height

def sendMails(distance_value):
    #send email to users
    page = auth.list_users()
    mail_list = []
    while page:
        for user in page.users:
            mail_list.append(user.email)
        # Get next batch of users.
        page = page.get_next_page()
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ", ".join(mail_list)
    msg['Subject'] = 'Rivertracker alert: Device ' + str(device_id) + ' is reporting abnormal readings! ' + str(distance_value) + " cm."

    body = "We detected that device # " + str(device_id) + ' is reporting abnormal readings: ' + str(distance_value) + " cm.\nhttps://river-tracker-295612.web.app/"
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    print("The login was done succesfully !")
    server.sendmail(email, mail_list, text)
    print("The email was sent to ", mail_list)

def check(distance_value):
    low_bound, high_bound, river_height = get_bounds(device_id)
    if not low_bound <= distance_value <= high_bound:
        sendMails(river_height*1000 + distance_value)
    
    
while True:
    now = datetime.now()
    dbCall()
    sleep(1800)
