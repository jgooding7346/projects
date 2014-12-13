import picamera,time,json

def getPicture(filename=""):
    picFine = True
    while picFine == True:
        if filename == "":
            picFine = True
            filename = input("Please give a valid filename").lower()
        else: 
            picFine = False
    while picFine != True:
        try:
            with picamera.PiCamera() as camera:
                camera.start_preview()
                time.sleep(2)
                camera.capture(filename+".jpg")
                camera.stop_preview()
                fileName = filename+".jpg"
                print('Captured {0}{1}'.format(filename,".jpg"))
            picFineInput = input("Is this ok? ").lower()
            if picFineInput == "yes" or picFineInput == "y":
                picFine = True
            else:
                picFine = False
        except picamera.exc.PiCameraError:
            print("There is a problem with the camera, please check it is connected")
            fileName = ""
        return fileName

def getCharProfile():
    #VARIABLES
    nameFine = False
    hairColourFine = False
    hatFine = False
    eyeColourFine = False
    genderFine = False
    facialHairFine = False
    glassesFine = False
    
    #NAME
    while nameFine != True:
        name = input("What is your name?  ").lower()
        if name == "":
            nameFine = False
        else:
            nameFine = True

    #PICTURE
    getPicture(name)

    #HAIR COLOUR
    while hairColourFine != True:
        hairColour = input("What is your hair colour?  ").lower()
        if hairColour == "":
            hairColourFine = False
        elif hairColour == "blonde":
            hairColourFine = True
        elif hairColour == "ginger":
            hairColourFine = True
        elif hairColour == "brown":
            hairColourFine = True
        elif hairColour == "grey":
            hairColourFine = True
        elif hairColour == "back":
            hairColourFine = True
        elif hairColour == "bald":
            hairColourFine = True
        else:
            hairColourFine = False

    #HAT
    while hatFine != True:
        hat  = input("Are you wearing a hat?  ").lower()
        if hat == "":
            hatFine = False
        elif hat == "yes":
            hat = True
            hatFine =  True
        elif hat == "no":
            hat = False
            hatFine = True
        else:
            hatFine = False

    #EYE COLOUR
    while eyeColourFine != True:
        eyeColour = input("What colour are your eyes?  ").lower()
        if eyeColour == "":
            eyeColourFine = False
        elif eyeColour == "blue":
            eyeColourFine = True
        elif eyeColour == "brown":
            eyeColourFine = True
        elif eyeColour == "green":
            eyeColourFine = True
        elif eyeColour == "grey":
            eyeColourFine = True
        else:
            eyeColourFine = False

    #GENDER
    while genderFine != True:
        gender = input("What gender are you? ").lower()
        if gender == "":
            genderFine = False
        elif gender == "m" or gender == "male":
            gender = "male"
            genderFine = True
        elif gender == "f" or gender == "female":
            gender = "female"
            genderFine = True
        else:
            genderFine = False

    #FACIAL HAIR
    while facialHairFine != True:
        facialHair = input("Do you have any facial hair? ").lower()
        if facialHair == "":
            facialHairFine = False
        elif facialHair == "yes":
            facialHair = True
            facialHairFine = True
        elif facialHair == "no":
            facialHair = False
            facialHairFine = True
        else:
            facialHairFine = False

    #GLASSES
    while glassesFine != True:
        glasses = input("Do you have glasses? ").lower()
        if glasses == "":
            glassesFine = False
        elif glasses == "yes" or glasses == "y":
            glasses = True
            glassesFine = True
        elif glasses == "no" or glasses == "n":
            glasses = False
            glassesFine = True
        else:
            glassesFine = False
    global profile
    profile = [name, hairColour, hat, eyeColour, gender, facialHair, glasses, name+".jpg"]
    
def saveProfile():
    getCharProfile()
    profiles.append(profile)
    with open("profiles.txt",mode="w") as p:
        json.dump(profiles,p)
def loadProfile():
    try:
        with open("profiles.txt",mode="r") as p:
            profiles = json.load(p)
    except IOError:
        print("profiles.txt not found. Creating a new profile")
        global profiles
        profiles=[]
        saveProfile()
