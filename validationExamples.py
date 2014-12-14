userName = "" #Assigns the variable userName as an empty string
while userName == "": #Loops until userName is not empty
    userName = input("What is your name? ") #Asks for a name to assign to an input
    password = "Ipswich" #Assigns the variable password as Ipswich
    passwordGuess = "" #Assigns the variable passwordGuess as an empty string
    while password != passwordGuess: #Loops until passwordGuess is not empty
        passwordGuess = input("What is the password? ") #Asks the user for a password
print("Good Morning "+userName) #Method one of printing with a variable
print("Good Morning %s" %userName) #Method 2 of printing with a variable
print("Good Morning {0}".format(userName)) #Method 3 of printing with a variable

