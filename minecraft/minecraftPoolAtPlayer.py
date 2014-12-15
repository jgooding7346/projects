import time,mcpi.minecraft as minecraft #Imports the modules time and mcpi.minecraft
mc = minecraft.Minecraft.create() #Locates an open Minecraft world

x,y,z=mc.player.getPos() #Assigns the player's position to the variables x, y and z


mc.setBlocks(x , y , z , x-10 , y-10 , z-25 , 20) #Places glass blocks between the player's x, y, z and 10 blocks away on the x axis, 10 blocks away on the y axis and 25 blocks away on the z axis
mc.setBlocks(x-1 , y , z-1 , x-9 , y-9 , z-24 , 9) #Places water blocks from 1 block away from the player on the x and z axes and the player's y position to 9 blocks from the player on the x axis, 9 blocks away from the player on the y axis and 24 blocks away on the z axis
mc.postToChat("Built") #Outputs "Built" to the in-game chat
