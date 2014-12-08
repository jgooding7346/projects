import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    block = 0
    mc.setBlocks(x-1,y,z-1,x+1,y+2,z+1,block)
