import time,picamera
picFine = False
while picFine != True:
    filename = input("What is your name? ")
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(filename+".jpg")
        camera.stop_preview()
        print('Captured %s' % filename)
    picFineInput = input("Is this ok?").lower()
    if picFineInput == "yes" or picFineInput == "y":
        picFine = True
    else:
        picFine = False

#SEE piCamTimelapse.py FOR COMMENTED VERSION
