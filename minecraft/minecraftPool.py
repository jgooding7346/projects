import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

mc.setBlocks(-52,0,-1,-50,0,10,20)
mc.setBlocks(-52,1,-1,-50,10,10,0)
mc.setBlocks(-53,0,10,-49,5,5,5)
mc.setBlocks(-52,1,9,-50,4,6,0)
mc.setBlock(-51,1,5,64)
mc.setBlock(-51,1,5,64,5)
mc.setBlocks(-57 , 0 , -2 , -47 , -10 , -27 , 20)
mc.setBlocks(-56 , 0 , -3 , -48 , -9 , -26 , 9)
mc.postToChat("Built")
