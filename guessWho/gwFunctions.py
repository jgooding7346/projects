import picamera,time

def getPicture(filename):
    picFine = False
    while picFine != True:
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(filename+".jpg")
            camera.stop_preview()
            print('Captured {0}{1}'.format(filename,".jpg"))
        picFineInput = input("Is this ok?").lower()
        if picFineInput == "yes" or picFineInput == "y":
            picFine = True
        else:
            picFine = False
