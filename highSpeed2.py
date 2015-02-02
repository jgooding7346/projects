#PiBOOM - Pi Bangs Or Other Mishaps

import picamera, RPi.GPIO as GPIO, time
button = 14
balloon = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)
GPIO.output(balloon, False)
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = (90)
    camera.start_preview()
    camera.start_recording("PiNuke.h264")
    print("Ready to fire.")
    GPIO.wait_for_edge(button, GPIO.FALLING)
    GPIO.output(balloon, True)
    time.sleep(5)
    GPIO.output(balloon, False)
    time.sleep(15)
    camera.stop_recording()
