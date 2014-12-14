import picamera,time #Imports the modules picamera and time

with picamera.Picamera() as camera: #Sets up the camera
    camera.resolution = (1024,768) #Sets the camera resolution
    camera.start_preview() #Starts the preview
    time.sleep(2) #Sleeps for 2 seconds
    camera.capture("PiCameraStuff.jpg") #Saves the image as PiCameraStuff.jpg
