#SEE minecraftTeleport.py FOR THE COMPLETE AND COMMENTED VERSION


import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
time.sleep(3)
mc.postToChat("5 seconds to teleport")
time.sleep(1)
mc.postToChat("4 seconds to teleport")
time.sleep(1)
mc.postToChat("3 seconds to teleport")
time.sleep(1)
mc.postToChat("2 seconds to teleport")
time.sleep(1)
mc.postToChat("1 seconds to teleport")
time.sleep(1)
mc.postToChat("Teleporting...")
mc.player.setPos(-1.7 , 10.0 , 18.9)
