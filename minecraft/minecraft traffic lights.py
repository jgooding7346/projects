import mcpi.minecraft as minecraft,time #Imports the modules mcpi.minecraft and time
mc = minecraft.Minecraft.create()

mc.player.setPos(0.5,0,2)

black=7 #Assigns the value 7 to the variable black
red=14 #Assigns the value 14 to the variable red
amber=1 #Assigns the value 1 to the variable amber
green=5 #Assigns the value 5 to the variable green

for y in range(5): #Loops 6 times
    mc.setBlock(0,y,0,35,black) #Places blocks of black wool at y values from 0 to 5

while True: #Loops forever
    mc.setBlock(0,5,0,35,red) #Places a red wool block at the given coordinate
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,3,0,35,black)
    time.sleep(10) #Sleeps for 10 seconds 
    mc.setBlock(0,5,0,35,red)
    mc.setBlock(0,4,0,35,amber)
    mc.setBlock(0,3,0,35,black)
    time.sleep(2) #Sleeps for 2 seconds
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,3,0,35,green)
    time.sleep(10) #Sleeps for 10 seconds
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,4,0,35,amber)
    mc.setBlock(0,3,0,35,black)
    time.sleep(3) #Sleeps for 10 seconds
