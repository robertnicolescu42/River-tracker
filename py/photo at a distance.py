from picamera import PiCamera, Color
import RPi.GPIO as GPIO
import time
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime



camera = PiCamera()
def preview():
    camera.rotation = 180

    camera.start_preview(alpha = 200)
    sleep(5)
    camera.stop_preview()

def takePic(text = "no distance aquired"):
    camera.rotation = 180
    camera.resolution = (2592, 1944)
    camera.start_preview()
    camera.annotate_text = "Approx. distance: ~" + text + " cm"
    camera.annotate_foreground = Color('black')
    camera.annotate_background = Color('white')
    camera.annotate_text_size = 120
    
    now = datetime.now()
    dt_string = now.strftime("%d %m %Y_%H:%M:%S")
    path = '/home/pi/Projects/Licenta/py/photos/%s.jpg' % dt_string
    camera.capture(path)
    camera.stop_preview()
    return path
    
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
        print(f'{doc.id} => {doc.to_dict()}')

def addDistance(distance_value, path):
    doc_ref = db.collection(u'distances')
    doc_ref.add({
        u'distance': distance_value,
        u'photo_path': path
    })
    
#addDistance(distance())

#readDistances()

def dbCall():
    distance_value, path = photoWithDistance()
    addDistance(distance_value, path)
    readDistances()
    
dbCall()