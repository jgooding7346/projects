import time,mcpi.minecraft as minecraft,random #Imports the time, mcpi.minecraft and random modules
mc = minecraft.Minecraft.create() #Locates an open Minecraft world
while True: #Loops forever
    pos = mc.player.getPos() #Gets the player's position
    x = pos.x #Assigns the player's x position to the variable x
    y = pos.y #Assigns the player's y position to the variable y
    z = pos.z #Assigns the player's z position to the variable z
    water = 9 #Assigns the value 9 to the variable water
    xW = random.randint(int(pos.x-10),int(pos.x+10)) #Assigns a random number up to 10 from the player's x value to the variable xW
    yW = y + 50 #Assigns the value of the player's y position + 50 to the variable yW
    zW = random.randint(int(pos.z-10),int(pos.z+10)) #Assigns a random number up to 10 from the player's z value to the variable zW
    mc.setBlock(xW , yW , zW , water) #Places a water block at the coordinate defined by xW, yW and zW
    mc.setBlock(xW , yW+1 , zW , 35) #Places a wool block at the coordinate above the water block
    time.sleep(2) #Sleeps for 2 seconds
    mc.setBlocks(x-10 , y+50 , z-10 , x+10 , y+51 , z+10, 0) #clears all blocks 10 blocks away from the player at their y + 50
    
