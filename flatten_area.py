from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

position = mc.player.getPos()

# Grass under foot
mc.setBlocks(position.x - 20,
             position.y -1,
             position.z -20,
             position.x + 20,
             position.y -1,
             position.z +20,
             block.GRASS.id
            )

# Air above
mc.setBlocks(position.x - 20,
             position.y,
             position.z -20,
             position.x + 20,
             position.y + 50,
             position.z +20,
             block.AIR.id
            )
