# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block

# connect to minecraft
mc = Minecraft.create()

# get the x,y,z (position)
position = mc.player.getTilePos()

# create stone cube
mc.setBlocks(position.x+2, position.y, position.z,
             position.x+6, position.y+3, position.z+3,
             block.STONE.id)

# hollow out with air
mc.setBlocks(position.x+3, position.y, position.z+1,
             position.x+5, position.y+2, position.z+2,
             block.AIR.id)

# build door
mc.setBlock(position.x+4, position.y, position.z,
            block.DOOR_WOOD.id, 1)
mc.setBlock(position.x+4, position.y+1, position.z,
            block.DOOR_WOOD.id, 9)

# place bed
mc.setBlock(position.x+3, position.y, position.z+1,
            block.BED.id, 0)
mc.setBlock(position.x+3, position.y, position.z+2,
            block.BED.id, 8)

# place chest
mc.setBlock(position.x+5, position.y, position.z+2,
            block.CHEST.id, 4)

# place crafting table
mc.setBlock(position.x+5, position.y, position.z+1,
            block.CRAFTING_TABLE.id, 0)

# torch
mc.setBlock(position.x+4, position.y+1, position.z+2,
            block.TORCH.id, 4)
