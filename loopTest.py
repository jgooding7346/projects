import time,mcpi.minecraft as minecraft #Imports the modules time and mcpi.minecraft

number=1 #Assigns the variable number as 1
while number < 5: #Loops until number is equal to or more than 5
    global number #makes number a global variable
    number + 1 #Adds 1 to number
    time.sleep(0.05) #Sleeps for 5% of a second

if number >= 5: #Checks if number is equal to or more than 5
    print "Done" #Outputs "Done"
