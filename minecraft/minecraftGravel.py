import time,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()
while True: #Causes a loop to occur
    pos = mc.player.getPos() #Gets the player's location
    mc.setBlock(random.randint(int(pos.x-10),int(pos.x+10)),pos.y+50,random.randint(int(pos.x-10),int(pos.x+10)),13)
    time.sleep(0.05)
