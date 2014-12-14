import time,mcpi.minecraft as minecraft #Imports the modules time and mcpi.minecraft
mc = minecraft.Minecraft.create() #Locates an open Minecraft world

playerPos = mc.player.getPos() #Gets the player's position
x = playerPos.x #Assigns the player's x coordinate to the variable X
y = playerPos.y #Assigns the player's y coordinate to the variable Y
z = playerPos.z #Assigns the player's z coordinate to the variable Z

def house(x,y,z): #Defines the function house with the parameters x, y and z
    mc.setBlocks(x-3,y-1,z-2,x+3,y+6,z+2,45) #build blocks between the given coordinates
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
    
for xPos in (0,10,20,30,40,50,60,70,80): #Uses the iterator xPos set at intervals of 10 between 0 and 80
    for zPos in (0,10,20,30,40,50,60,70,80): #Uses the iterator zPos set at intervals of 10 between 0 and 80
        house(xPos,y,zPos) #Calls the house function and builds a house using xPos, y and zPos as the parameters
    
