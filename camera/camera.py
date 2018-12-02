from picamera import PiCamera
import time

def run():
    video()

def pic():
    """set camera"""
    camera = PiCamera()
    camera.resolution = (1920,1080)
    camera.framerate = 60
    camera.start_preview()
    camera.capture('/home/pi/testme.jpg')
    camera.stop_preview()

def video():
 
    camera = PiCamera()
    camera.start_preview()
    camera.vflip = True
    camera.hflip = True
    camera.brightness = 60
   
    camera.start_recording('video.h264')
    time.sleep(30)
    camera.stop_recording()

