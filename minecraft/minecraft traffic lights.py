import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

mc.player.setPos(0.5,0,2)

black=7
red=14
amber=1
green=5

mc.setBlock(0,0,0,35,black)
mc.setBlock(0,1,0,35,black)
mc.setBlock(0,2,0,35,black)
mc.setBlock(0,3,0,35,black)
mc.setBlock(0,4,0,35,black)
mc.setBlock(0,5,0,35,black)

while True:
    mc.setBlock(0,5,0,35,red)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,3,0,35,black)
    time.sleep(10)
    mc.setBlock(0,5,0,35,red)
    mc.setBlock(0,4,0,35,amber)
    mc.setBlock(0,3,0,35,black)
    time.sleep(2)
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,3,0,35,green)
    time.sleep(10)
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,4,0,35,amber)
    mc.setBlock(0,3,0,35,black)
    time.sleep(3)
