import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y-1
    z = pos.z
    block = 41
    mc.setBlock(x,y,z,block)
    
