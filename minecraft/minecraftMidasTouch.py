import time,mcpi.minecraft as minecraft #Imports the time and mcpi.minecraft modules
mc = minecraft.Minecraft.create() #Locates an open Minecraft world
while True: #Loop forever 
    pos = mc.player.getPos() #Get the player position
    x = pos.x #Assigns the player's x position to the variable x
    y = pos.y-1 #Assigns the player's y position - 1 to the variable y
    z = pos.z #Assigns the player's z position to the variable z
    block = 41#Assigns the value 41 to the variable block
    mc.setBlock(x,y,z,block) #Places a gold block at the position directly beneath the player
    
