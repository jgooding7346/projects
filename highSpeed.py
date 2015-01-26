import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = (90)
    camera.start_recording("PiStuff.h264")
    camera.wait_recording(60)
    camera.stop_recording()
