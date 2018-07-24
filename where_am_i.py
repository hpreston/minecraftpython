# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

# connect to minecraft
mc = Minecraft.create()

# repeat this program always
while True:
    # 1) get current position of player
    #    and print to screen
    position = mc.player.getTilePos()
    print("x: {}, y: {}, z: {}".format(position.x,
                                       position.y,
                                       position.z))

    # 2) what block is player "in"
    # "lists" of block ids types
    air = [0]
    water = [8,9]
    lava = [10,11]

    # get block id of "feet"
    block_player_in = mc.getBlock(position)

    # "test" if player standing in block types
    if block_player_in in air:
        print("Player is in air.")
    elif block_player_in in water:
        print("player is in water")
    elif block_player_in in lava:
        print("OW OW OW OW OW (You are in lava)")
    else:
        print("player is in block id {}".format(block_player_in))

    # 3) what block is player "on"
    block_player_on = mc.getBlock(position.x,
                                  position.y -1,
                                  position.z)
    # "list" of different types of stone
    types_of_stone = [
        block.STONE.id,
        block.COBBLESTONE.id,
        block.GRAVEL.id,
        block.SANDSTONE.id
    ]

    # "test" what type of block player standing on
    if block_player_on in types_of_stone:
        print("player is on stone")
    elif block_player_on == block.GRASS.id:
        print("player is on grass")
    elif block_player_on ==block.AIR.id:
        print("YOU ARE FLYING OMG!")
    else:
        print("player is on block id {}".format(block_player_in))

    # pause for 1 second
    sleep(1)
