# encoding: utf-8
import RPi.GPIO
import time
import common.common as comm

RED_LIGHT=38
RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(RED_LIGHT, RPi.GPIO.OUT)

def run():
    for i in range(1,10):
        batch()
        time.sleep(1)

def batch():
    comm.blink_light(RED_LIGHT,rank=50,turn_cnt=1,interval=0.04)
