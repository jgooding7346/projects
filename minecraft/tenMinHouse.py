import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

playerPos = mc.player.getPos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

def house(x,y,z):
    mc.setBlocks(x-3,y-1,z-2,x+3,y+6,z+2,45)
    mc.setBlocks(x-2,y,z-1,x+2,y+5,z+1,0)
    mc.setBlocks(x-2,y-1,z-1,x+3,y-1,z+1,5)
    mc.setBlocks(x-3,y+1,z,x-3,y+4,z,20)
    mc.setBlocks(x+3,y+1,z,x+3,y+4,z,20)
    mc.setBlocks(x,y,z+2,x,y+1,z+2,0)
    mc.setBlocks(x-3,y+6,z-2,x+3,y+6,z+2,108)
    mc.setBlocks(x,y,z+2,x,y+1,z+2,0)
    mc.setBlocks(x,y-1,z+3,x,y-1,z+5,1)
    mc.setBlocks(x,y-1,z+3,x+5,y+1,z+5,0)
    mc.setBlocks(x,y-1,z+3,x+5,y-1,z+5,1)
    mc.setBlocks(x,y-1,z+3,x-5,y+1,z+5,0)
    mc.setBlocks(x,y-1,z+3,x-5,y-1,z+5,1)
    mc.setBlocks(x+4,y-1,z+3,x+5,y+1,z+5,0)
    mc.setBlocks(x+4,y-1,z-4,x+5,y-1,z+5,1)
    mc.setBlocks(x-4,y-1,z+3,x+5,y+1,z+5,0)
    mc.setBlocks(x-4,y-1,z+7,x+5,y-1,z+5,1)
    
for xPos in (0,10,20,30,40,50,60,70,80):
    for zPos in (0,10,20,30,40,50,60,70,80):
        house(xPos,y,zPos)
    
