import mcpi.minecraft as minecraft,random,time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos() #Assigns the variable pos to the player's position
spacePos = mc.player.getPos() #Assigns the variable spacePos (Space Invader (SI) Position) to the player's position 
spaceX = int(spacePos.x+random.randint(-64,64)) #Assigns spaceX (SI x coordinate) to up to 64 blocks from the player
spaceY = int(spacePos.y+random.randint(-32,32)) #Assigns spaceY (SI y coordinate) to up to 64 blocks from the player
spaceZ = int(spacePos.z+random.randint(-64,64)) #Assigns spaceZ (SI z coordinate)  to up to 64 blocks from the player
spaceChatPos = spaceX,spaceY,spaceZ #Assigns spaceX, spaceY, spaceZ to the variable which will be posted to chat
mc.postToChat(spaceChatPos) #Posts spaceChatPos to chat
print(spaceChatPos) #Prints spaceChatPos so that player has permanent copy of SI coordinates

#This section builds a space invader around the coordinates spaceX, spaceY, spaceZ with 0 of the SI being the very centre
mc.setBlocks(spaceX-6,spaceY-4,spaceZ-1,spaceX+6,spaceY+4,spaceZ+1,0) 
mc.setBlocks(spaceX-5,spaceY,spaceZ,spaceX+5,spaceY,spaceZ,35,5)
mc.setBlocks(spaceX-3,spaceY-1,spaceZ,spaceX+3,spaceY-1,spaceZ,35,5)
mc.setBlocks(spaceX-4,spaceY+1,spaceZ,spaceX-3,spaceY+1,spaceZ,35,5)
mc.setBlocks(spaceX+4,spaceY+1,spaceZ,spaceX+3,spaceY+1,spaceZ,35,5)
mc.setBlocks(spaceX-3,spaceY+2,spaceZ,spaceX+3,spaceY+2,spaceZ,35,5)
mc.setBlocks(spaceX-5,spaceY-1,spaceZ,spaceX-5,spaceY-2,spaceZ,35,5)
mc.setBlocks(spaceX+5,spaceY-1,spaceZ,spaceX+5,spaceY-2,spaceZ,35,5)
mc.setBlock(spaceX-3,spaceY-2,spaceZ,35,5)
mc.setBlock(spaceX+3,spaceY-2,spaceZ,35,5)
mc.setBlocks(spaceX-2,spaceY-3,spaceZ,spaceX-1,spaceY-3,spaceZ,35,5)
mc.setBlocks(spaceX+2,spaceY-3,spaceZ,spaceX+1,spaceY-3,spaceZ,35,5)
mc.setBlock(spaceX-2,spaceY+3,spaceZ,35,5)
mc.setBlock(spaceX+2,spaceY+3,spaceZ,35,5)
mc.setBlock(spaceX-3,spaceY+4,spaceZ,35,5)
mc.setBlock(spaceX+3,spaceY+4,spaceZ,35,5)
mc.setBlocks(spaceX+1,spaceY+1,spaceZ,spaceX-1,spaceY+1,spaceZ,35,5)
#End of construction section
#This section was kept separate from the function to avoid confusion whilst coding

def setRandomInvader(colour): #Defines a function named randomSpaceInvade to build a random space invader using the parameters
    pos = mc.player.getPos() #Assigns pos to the player's position again to get a refreshed position
    spacePos = mc.player.getPos() #Assigns spacePos to the player's position again to get a refreshed position
    spaceX = int(spacePos.x+random.randint(-64,64)) #Gets a new spaceX
    spaceY = int(spacePos.y+random.randint(-64,0)) #Gets a new spaceY
    spaceZ = int(spacePos.z+random.randint(-64,64)) #Gets a new spaceZ
    spaceChatPos = spaceX,spaceY,spaceZ #Re-assigns the spaceChatPos variable
    mc.postToChat("Space Invader Built at:") #Posts the text Space invader built at: to chat
    mc.postToChat(spaceChatPos) #Posts the variable spaceChatPos to chat
    print(spaceChatPos) #Prints the variable spaceChatPos
    mc.setBlocks(spaceX-6,spaceY-4,spaceZ-1,spaceX+6,spaceY+4,spaceZ+1,0)
    mc.setBlocks(spaceX-5,spaceY,spaceZ,spaceX+5,spaceY,spaceZ,35,colour)
    mc.setBlocks(spaceX-3,spaceY-1,spaceZ,spaceX+3,spaceY-1,spaceZ,35,colour)
    mc.setBlocks(spaceX-4,spaceY+1,spaceZ,spaceX-3,spaceY+1,spaceZ,35,colour)
    mc.setBlocks(spaceX+4,spaceY+1,spaceZ,spaceX+3,spaceY+1,spaceZ,35,colour)
    mc.setBlocks(spaceX-3,spaceY+2,spaceZ,spaceX+3,spaceY+2,spaceZ,35,colour)
    mc.setBlocks(spaceX-5,spaceY-1,spaceZ,spaceX-5,spaceY-2,spaceZ,35,colour)
    mc.setBlocks(spaceX+5,spaceY-1,spaceZ,spaceX+5,spaceY-2,spaceZ,35,colour)
    mc.setBlock(spaceX-3,spaceY-2,spaceZ,35,colour)
    mc.setBlock(spaceX+3,spaceY-2,spaceZ,35,colour)
    mc.setBlocks(spaceX-2,spaceY-3,spaceZ,spaceX-1,spaceY-3,spaceZ,35,colour)
    mc.setBlocks(spaceX+2,spaceY-3,spaceZ,spaceX+1,spaceY-3,spaceZ,35,colour)
    mc.setBlock(spaceX-2,spaceY+3,spaceZ,35,colour)
    mc.setBlock(spaceX+2,spaceY+3,spaceZ,35,colour)
    mc.setBlock(spaceX-3,spaceY+4,spaceZ,35,colour)
    mc.setBlock(spaceX+3,spaceY+4,spaceZ,35,colour)
    mc.setBlocks(spaceX+1,spaceY+1,spaceZ,spaceX-1,spaceY+1,spaceZ,35,colour)
    
xMatched = False
yMatched = False
zMatched = False
finished = False

while finished == False: #Sets an infinite loop running
    time.sleep(30)
    mc.postToChat("30 seconds remaining") #Posts the text 30 seconds remaining to chat
    mc.postToChat(spaceChatPos)
    time.sleep(30)
    playerPos = mc.player.getPos()
    if playerPos.x == spaceX+1 or playerPos.x == spaceX-1: #Checks if the player is in the right position on the x axis
        xMatched = True

    if playerPos.y == spaceY: #Checks if the player is in the right position on the y axis
        yMatched = True

    if playerPos.z == spaceZ+1 or playerPos.z == spaceZ-1: #Checks if the player is in the right position on the z axis
        zMatched = True

    if xMatched == True and yMatched == True and zMatched == True: #Checks if the player is in the correct position next to the space invader 
        mc.postToChat("Space Invader Found") #Posts the text Space Invader Found to chat
        finished=True #Ends the loop
    else:
        mc.postToChat("Time Exceearqy3tdfo") #USed to imitate a system malfunction
        time.sleep(0.1) #Pauses for 0.1 of a second
        mc.postToChat("erro3224, infect3245gui spread356887e54.....") #Continues the malfunction effect
        time.sleep(2.5) #Pauses for 2.5 seconds
        mc.postToChat("Commencing Deep Clean ") #Informs the player that blocks are going to be wiped
        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("0%") #Informs the player that the wipe is imininent
            
        for colour in range(9): #Loops the following 10 timwes with the iterator changing up to the number 10 and the iterator being called colour
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("10%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("20%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("30%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("40%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("50%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("60%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("70%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("80%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("90%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping Surrounding Blocks")
            mc.postToChat("100%")

        time.sleep(2.5)
        mc.setBlocks(pos.x-64,pos.y-64,pos.z-64,pos.x+64,pos.y+64,pos.z+64,0) #Wipes every block within 64 blocks of the player
        finished=True #Ends the loop
        exit #Ends the program
    exit
exit
