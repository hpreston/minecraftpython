# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block

# connect to minecraft
mc = Minecraft.create()

# get the x,y,z (position)
position = mc.player.getTilePos()

# teleport
# mc.player.setTilePos(-29,70,-8)
