import time,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    water = 9
    xW = random.randint(int(pos.x-10),int(pos.x+10))
    yW = y + 50
    zW = random.randint(int(pos.z-10),int(pos.z+10))
    mc.setBlock(xW , yW , zW , water)
    mc.setBlock(xW , yW+1 , zW , 35)
    time.sleep(2)
    mc.setBlocks(x-10 , y+50 , z-10 , x+10 , y+51 , z+10, 0)
    
