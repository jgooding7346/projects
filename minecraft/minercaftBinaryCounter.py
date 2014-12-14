import mcpi.minecraft as minecraft,time #Imports the Minecraft Pi and Time modules 
mc = minecraft.Minecraft.create() #Finds the open Minecraft world

mc.setBlocks(-30,-5,-30,30,30,30,0) #Removes all the blocks between -30,-5,-30 and 30,30,30

for b in range(7): #Loops 8 times with the iterator of b changing by 1 each time
    mc.setBlock(0,0,b,35,5)
    for b2 in range(7):
        mc.setBlock(1,0,b2,35,5)
        for b3 in range(7):
            mc.setBlock(2,0,b3,35,5)
            for b4 in range(7):
                mc.setBlock(3,0,b4,35,5)
                for b5 in range(7):
                    mc.setBlock(4,0,b5,35,5)
                    for b6 in range(7):
                        mc.setBlock(5,0,b5,35,5)
                        for b7 in range(7):
                            mc.setBlock(6,0,b7,35,5)
                            for b8 in range(7):
                                mc.setBlock(7,0,b8,35,5)
                            
