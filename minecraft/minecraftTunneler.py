import time,mcpi.minecraft as minecraft #Imports the modules time and mcpi.minecraft
mc = minecraft.Minecraft.create() #Locates an open Minecraft world
while True: #Loops forever
    pos = mc.player.getPos() #Gets the player's position
    x = pos.x #Assigns the player's x coordinate to the variable x
    y = pos.y #Assigns the player's y coordinate to the variable y
    z = pos.z #Assigns the player's z coordinate to the variable z
    block = 0 #Assigns the value 0 to the variable block
    mc.setBlocks(x-1,y,z-1,x+1,y+2,z+1,block) #Removes all blocks 1 block from the player on the same y coordinate as the player
