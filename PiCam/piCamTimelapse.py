import time, picamera #Imports the pi camera and time modules
picFine = False #Assigns the variable picFine as False
while picFine != True: #Loops whilst picFine is False
    with picamera.PiCamera() as camera: #Sets up the picamera
        camera.start_preview() #Starts the camera preview
        time.sleep(2) #Sleeps for 2 seconds
        filename = "cameraTest.jpeg" #Assigns the variable filename as "cameraTest.jpeg"
        camera.capture(filename) #Saves the picture under the name assigned to filename
        camera.stop_preview() #Ends the preview
        print('Captured %s' % filename) #Outputs "Captured cameraTest.jpeg"
    picFineInput = input("Is this Picture ok?").lower() #Asks the user if the picture is ok
    if picFineInput == yes or picFineInput == y: #Checks if picFineInput is "yes" or "y"
        picFine = True #Assigns the variable picFine as True
    else:
        picFine = False #Assigns the variable picFine as False
