# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block

# connect to minecraft
mc = Minecraft.create()

# get the x,y,z (position)
position = mc.player.getTilePos()

# list of relative coordinates for wall
coords = [
    [ -1, 0, +1],
    [ 0, 0, +1],
    [ +1, 0, +1],
    [-1, 0, 0],
    [+1, 0, 0],
    [-1, 0, -1],
    [0, 0, -1],
    [+1, 0, -1]
]

# loop over each coordinate
for i in coords:
    # set blocks at relative positions 
    mc.setBlock(
        position.x + i[0],
        position.y + i[1],
        position.z + i[2],
        block.BRICK_BLOCK.id
    )
