# encoding: utf-8
import RPi.GPIO
import time

RED_LIGHT=38
RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(RED_LIGHT, RPi.GPIO.OUT)

pwm = RPi.GPIO.PWM(RED_LIGHT, 70)

pwm.start(0)

try:
    idx = 100
    num = 0
    while num < idx:
        for i in xrange(0, 101, 20):
            print(i)
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in xrange(100, -1, -20):
            print(i)
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
        num = num + 1
except KeyboardInterrupt:
	pass

pwm.stop()
RPi.GPIO.cleanup()

