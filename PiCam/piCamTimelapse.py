import time
import picamera
picFine = False
while picFine != True:
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture
        camera.start_preview
        print('Captured %s' % filename)
    picFineInput = input("Is this Picture ok?").lower()
    if picFineInput == yes or picFineInput == y:
        picFine = True
    else:
        picFine = False
