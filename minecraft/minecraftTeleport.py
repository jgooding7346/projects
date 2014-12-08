import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(3)
mc.postToChat("3 Seconds to teleport")
time.sleep(1)
mc.postToChat("2 Seconds to teleport")
time.sleep(1)
mc.postToChat("1 Seconds to teleport")
time.sleep(1)
mc.postToChat("Teleporting")

def teleport():
    mc.player.setPos(-1.5,17,-16.7)
    time.sleep(0.25)
    mc.player.setPos(-1.5,17,18.1)
    time.sleep(0.25)
    mc.player.setPos(-1.5,17,-6.3)
    mc.postToChat("Teleportation Complete")
    time.sleep(0.25)
    
while True:
    teleport()
