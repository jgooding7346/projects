import random,time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

x = random.randint(-128,128)
y = random.randint(-128,-1)
z = random.randint(-128,128)

block = 38
mc.setBlock(x,y,z,block)

while True:
    mc.postToChat((x,y,z) - mc.player.getPos())
    time.sleep(0.5)
