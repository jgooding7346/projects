import time,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()
while True: #Causes a loop to occur
    pos = mc.player.getPos() #Gets the player's location
    mc.setBlock(random.randint(int(pos.x-10),int(pos.x+10)),pos.y+50,random.randint(int(pos.x-10),int(pos.x+10)),13) #Places a block 10 blocks away o the x and z axes and 50 blocks above the player
    time.sleep(0.05) #Sleeps for 5% of a second
