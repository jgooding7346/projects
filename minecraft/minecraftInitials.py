import time,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
def initials(x,y,z,colour):
    mc.setBlocks(x+1,y,z,x+13,y+6,z,0)
    mc.setBlocks(x+4,y+6,z,x+6,y+6,z,35,colour)
    mc.setBlocks(x+5,y+5,z,x+5,y+1,z,35,colour)
    mc.setBlocks(x+3,y,z,x+4,y,z,35,colour)
    mc.setBlock(x+2,y+1,z,35,colour)
    mc.setBlocks(x+8,y+1,z,x+8,y+5,z,35,colour)
    mc.setBlocks(x+9,y,z,x+11,y,z,35,colour)
    mc.setBlocks(x+11,y+2,z,x+12,y+1,z,35,colour)
    mc.setBlock(x+11,y+1,z,0)
    mc.setBlocks(x+9,y+6,z,x+11,y+6,z,35,colour)
    mc.setBlock(x+12,y+5,z,35,colour)

def a(x,y,z,colour):
    mc.setBlocks(x+1,y,z,x+1,y+6,z,35,colour)
    mc.setBlocks(x+5,y,z,x+5,y+6,z,35,colour)
    mc.setBlocks(x+2,y+4,z,x+4,y+4,z,35,colour)
    mc.setBlocks(x+2,y+7,z,x+4,y+7,z,35,colour)

def one(x,y,z,colour):
    mc.setBlocks(x+1,y,z,x+3,y,z,35,colour)
    mc.setBlocks(x+2,y,z,x+2,y+7,z,35,colour)
    mc.setBlock(x+1,y+6,z,35,colour)

for colour in (range(6,11)):
    initials(x,y,colour,colour)


a(20,20,20,2)
one(10,10,30,1)
