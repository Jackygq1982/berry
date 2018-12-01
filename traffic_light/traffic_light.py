import RPi.GPIO as GPIO
import time
import common.common as comm

RED = 36
YELLOW = 38
GREEN = 40
GPIO.setmode(GPIO.BOARD)

def init():
    GPIO.cleanup()
    GPIO.setup(RED,GPIO.OUT)
    GPIO.setup(GREEN,GPIO.OUT)
    clean()

def clean():
    shut_down(GREEN)
    shut_down(RED)

def run():
    init()
    is_red = True
    for i in xrange(0,5):
        batch(is_red)
        time.sleep(1)
        clean()
        is_red = not is_red

def light_up(pin_code):
    GPIO.output(pin_code,GPIO.HIGH)

def shut_down(pin_code):
    GPIO.output(pin_code,GPIO.LOW)

def batch(is_red):
    if is_red:
        light_up(RED)
        time.sleep(2)
        comm.blink_light(YELLOW,rank=5,turn_cnt=3,interval=0.04)
        shut_down(RED)
        light_up(GREEN)
        time.sleep(2)
        shut_down(GREEN)
    if not is_red:
        light_up(GREEN)
        time.sleep(2)
        comm.blink_light(YELLOW,rank=5,turn_cnt=3,interval=0.04)
        shut_down(GREEN)
        light_up(RED)
        time.sleep(2)
        shut_down(RED)
