import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getPos()
    if pos.y < -10 or pos.y > 50:
        mc.player.setPos(pos.x+1,20,pos.z+1)
