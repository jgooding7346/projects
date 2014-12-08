import picamera,time

for run in range(4):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        name = input("What is your name?")
        camera.start_preview()
        time.sleep(2)
        camera.capture(name + ".jpeg")
