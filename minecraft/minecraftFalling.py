import random,time,mcpi.minecraft as minecraft #Imports the time and mcpi.minecraft modules
mc = minecraft.Minecraft.create() #Locates an open Minecraft world

x = random.randint(-128,128) #Selects a random point on the x axis and assigns this to the variable x
y = random.randint(-128,-1) #Selects a random point between -1 and -128 on the y axis and assigns this to the variable y
z = random.randint(-128,128) #Selects a random point on the z axis and assigns this to the variable z

block = 38 #Assigns the value 38 to the variable block
mc.setBlock(x,y,z,block) #Places a block at the point defined by the variables x, y and z

while True: #Loops forever
    mc.postToChat((x,y,z) - mc.player.getPos()) #Outputs the player's distance from the block on each axis
    time.sleep(0.5) #Sleeps for 50% of a second
