import time,mcpi.minecraft as minecraft #Imports the modules time and mcpi.minecraft
mc = minecraft.Minecraft.create() #Locates an open Minecraft world

time.sleep(3) #Sleeps for 3 seconds
mc.postToChat("3 Seconds to teleport") #Outputs "3 Seconds to teleport" to the in-game chat
time.sleep(1) #Sleeps for 1 seconds
mc.postToChat("2 Seconds to teleport") #Outputs "2 Seconds to teleport" to the in-game chat
time.sleep(1) #Sleeps for 1 seconds
mc.postToChat("1 Seconds to teleport") #Outputs "1 Seconds to teleport" to the in-game chat
time.sleep(1) #Sleeps for 1 seconds
mc.postToChat("Teleporting...") #Outputs "Teleporting..." To the in-game chat

def teleport(): #Defines the function teleport with no parameters
    mc.player.setPos(-1.5,17,-16.7) #Teleports the player to -1.5, 17. 16.7
    time.sleep(0.25) #Sleeps for 25% of a second
    mc.player.setPos(-1.5,17,18.1) #Teleports the player to -1.5, 17, 18.1
    time.sleep(0.25) #Sleeps for 25% of a second
    mc.player.setPos(-1.5,17,-6.3) #Teleports the player to -1.5, 17, -6.3
    mc.postToChat("Teleportation Complete") #Outputs "Teleportation Complete" tot the in-game chat
    time.sleep(0.25) #Sleeps for 25% of a second
    
while True: #Loops Forever
    teleport() #Calls the function teleport()
