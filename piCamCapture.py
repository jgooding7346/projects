import picamera,time #Imports the modules picamera and time

for run in range(4): #Runs a loop a set number of times
    with picamera.PiCamera() as camera: #Sets up the camera
        camera.resolution = (1024,768) #Sets the camera resolution
        name = input("What is your name?") #Asks for the user's name
        camera.start_preview() #Starts the camera preview
        time.sleep(2) #Sleeps for 2 seconds
        camera.capture(name + ".jpeg") #Saves a picture as the user's name with the .jpeg suffix
