import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

x,y,z=mc.player.getPos()


mc.setBlocks(x , y , z , x-10 , y-10 , z-25 , 20)
mc.setBlocks(x-1 , y , z-1 , x-9 , y-9 , z-24 , 9)
mc.postToChat("Built")
