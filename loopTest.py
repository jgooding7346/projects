import time,mcpi.minecraft as minecraft

number=1
while number < 5:
    global number
    number + 1
    time.sleep(0.05)

if number >= 5:
    print "Done"
