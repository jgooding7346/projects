import random,time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getPos() #Assigns the variable pos to the player's position
spacePos = mc.player.getPos() #Assigns the variable spacePos (Space Invader Position) to the player's position 
spaceX = int(spacePos.x+random.randint(-64,64)) #Assigns spaceX (SI x coordinate) to up to 64 blocks from the player
spaceY = int(spacePos.y+random.randint(-64,0)) #Assigns spaceY (SI y coordinate) to up to 64 blocks from the player
spaceZ = int(spacePos.z+random.randint(-64,64)) #Assigns spaceZ (SI z coordinate)  to up to 64 blocks from the player
spaceChatPos = spaceX,spaceY,spaceZ
mc.postToChat(spaceChatPos)
print(spaceChatPos)

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

def setRandomInvader(colour):
    pos = mc.player.getPos()
    spacePos = mc.player.getPos()
    spaceX = int(spacePos.x+random.randint(-64,64))
    spaceY = int(spacePos.y+random.randint(-64,0))
    spaceZ = int(spacePos.z+random.randint(-64,64))
    spaceChatPos = spaceX,spaceY,spaceZ
    mc.postToChat("Space Invader Built at:")
    mc.postToChat(spaceChatPos)
    print(spaceChatPos)
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

while True:
    time.sleep(30)
    mc.postToChat("30 seconds remaining")
    mc.postToChat(spaceChatPos)
    time.sleep(30)    
    playerPos = mc.player.getPos()
    if playerPos.x == spaceX+1 or playerPos.x == spaceX-1:
        xMatched = True

    if playerPos.y == spaceY:
        yMatched = True

    if playerPos.z == spaceZ+1 or playerPos.z == spaceZ-1:
        zMatched = True

    if xMatched == True and yMatched == True and zMatched == True:
        mc.postToChat("Space Invader Found")
    else:
        mc.postToChat("Time Exceearqy3tdfo")
        time.sleep(0.1)
        mc.postToChat("erro3224, infect3245gui spread356887e54.....")
        time.sleep(2.5)
        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("0%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("10%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("20%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("30%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("40%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("50%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("60%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("70%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("80%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("90%")

        for colour in range(9):
            setRandomInvader(colour)
            mc.postToChat("Wiping All Blocks")
            mc.postToChat("100%")

    exit
