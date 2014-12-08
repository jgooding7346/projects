import picamera,time

with picamera.Picamera() as camera:
    camera.resolution = (1024,768)
    camera.start_preview()

    time.sleep(2)
    camera.capture("PiCameraStuff.jpg")
