# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

# connect to minecraft
mc = Minecraft.create()

# get starting position coordinates
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# repeat the program always
while True:
    # pick new coordinates
    x += 100
    z += 100

    # teleport player to new location, print coordinates
    mc.player.setTilePos(x, y, z)
    print("Current Position: {}, {}, {}".format(x, y, z))

    # wait 5 seconds, and repeat
    sleep(5)
