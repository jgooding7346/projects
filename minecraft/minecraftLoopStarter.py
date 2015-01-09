import mcpi.minecraft as minecraft,time #Imports the Minecraft Pi and Time modules 
mc = minecraft.Minecraft.create() #Finds the open Minecraft world

mc.setBlocks(-30,-5,-30,30,30,30,0) #Removes all the blocks between -30,-5,-30 and 30,30,30

for b in range(15): #Causes a finite loop with the iterator as the numbers 0-14 
    for b2 in range(15):
        mc.postToChat(b) #Posts the current b
        mc.setBlock(b2,b2,b,35,b) #Sets the block at 0,b,0 to wwool of the colour which b is at that time
        print(b)
