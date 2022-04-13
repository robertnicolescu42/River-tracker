# River-tracker
https://drive.google.com/file/d/15pf6hBGVI41Zoq-URmmWe-80QxOVm8MP/view?usp=sharing

Steps:
- VScode:
  - cd rivertracker
  - npm i
  - npm run serve

- On raspberry pi:
  - connect the sensor and camera
  - download json with credentials from google cloud platform/firebase and put it in the py directory 
  - set a device id on "device_config.py"
  - set gmail up by enabling less secure apps and the login information in "config.py"
  - run "rivertracker with mail.py"
