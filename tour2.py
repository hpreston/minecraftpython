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

# block ids for testing
water = [block.WATER_FLOWING.id, block.WATER_STATIONARY.id]
lava = [block.LAVA_FLOWING.id, block.LAVA_STATIONARY.id]

# repeat the program always
while True:
    # pick new coordinates
    x += 100
    z += 100
    # put player on top of the heighest block
    y = mc.getHeight(x, z,)

    # find out the type of block player will stand on
    target_block_id = mc.getBlock(x, y-1, z)

    # test if the block is safe
    # if not, place an OBSIDIAN block below player
    if target_block_id in water:
        print("on water")
        mc.setBlock(x, y-1, z, block.OBSIDIAN.id)
    elif target_block_id in lava:
        print("on lava")
        mc.setBlock(x, y-1, z, block.OBSIDIAN.id)

    # teleport player to new location, print coordinates
    mc.player.setTilePos(x, y, z)
    print("Current Position: {}, {}, {}".format(x, y, z))

    # wait 5 seconds, and repeat
    sleep(5)
