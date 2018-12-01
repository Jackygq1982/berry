# encoding: utf-8
import RPi.GPIO as GPIO

import time

def blink_light(pin_code,rank=5,turn_cnt=1,interval=0.02):

    count = 100/5
    GPIO.setup(pin_code, GPIO.OUT)
    pwm = GPIO.PWM(pin_code, 70)
    pwm.start(0)
    try:
        num = 0
        while num < turn_cnt:
            for i in xrange(0, 101, count):
                pwm.ChangeDutyCycle(i)
                time.sleep(interval)
            for i in xrange(100, -1, count*-1):
                pwm.ChangeDutyCycle(i)
                time.sleep(interval)
            num = num + 1
    except KeyboardInterrupt:
        pass

    pwm.stop()
