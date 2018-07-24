# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

# connect to minecraft
mc = Minecraft.create()

# get starting position coordinates
position = mc.player.getTilePos()

# Create a stack of BEDROCK
mc.setBlock(position.x + 2,
            position.y,
            position.z,
            block.BEDROCK.id
           )
mc.setBlock(position.x + 2,
            position.y + 1,
            position.z,
            block.BEDROCK.id
           )
mc.setBlock(position.x + 2,
            position.y + 2,
            position.z,
            block.BEDROCK.id
           )
