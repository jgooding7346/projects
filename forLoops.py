import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

for block in (0,2,4,6,8,10):
    mc.setBlock(0,20,block,22)
    mc.postToChat(block)
    time.sleep(0.5)
    
for name in ("Harry","Bethany","Jo","Katy"):
    mc.postToChat(("Hello " , name)) 
