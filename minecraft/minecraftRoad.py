import mcpi.minecraft as minecraft #Imports the module mcpi.minecraft
mc = minecraft.Minecraft.create() #Locates an open Minecraft world

black=7 #Assigns the value 7 to the variable black
mc.setBlocks(-27,2,-8,-32,2,26,35,black) #Places black wool blocks between -27, 2, -8 and -32, 2, 26
