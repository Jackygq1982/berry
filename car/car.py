import RPi.GPIO as GPIO
LEFT1 = 17
LEFT2 = 18
LEFT3 = 27

RIGHT1 = 15
RIGHT2 = 16
RIGHT3 = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT1,GPIO.OUT)
GPIO.setup(LEFT2,GPIO.OUT)

GPIO.output(LEFT2,GPIO.HIGH)
GPIO.output(LEFT1,GPIO.LOW)
