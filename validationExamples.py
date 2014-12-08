userName = "" #Assigns the variable 
while userName == "":
    userName = input("What is your name? ")
    password = "Ipswich"
    passwordGuess = ""
    while password != passwordGuess:
        passwordGuess = input("What is the password? ")
print("Good Morning "+userName)
print("Good Morning %s" %userName)
print("Good Morning {0}".format(userName))

