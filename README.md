# Minecraft Python 
Sample Python scripts, notes, and example for using the Python mcpi library for manipulating and working with Minecraft.  I use these scripts and the library to explore Python with my son Alexander.  

## Getting Started 
You'll need a Minecraft setup that supports interaction via API.  This is most simply achieved with the Minecraft for Raspberry Pi, but can also work with full blown Minecraft Java Servers with the [Raspberry Juice Server](https://github.com/zhuowei/RaspberryJuice).  

> Details of setting up the server side are out of scope for these instructions, it is assumed you already have the server running and a game client connected.  

1. Clone down this repository.  

```bash
git clone https://github.com/hpreston/minecraftpython
cd minecraftpython
```

1. Setup a Python virtual environment.  Python 3 was used with these examples and is recommended (though Python 2 is supported by the library).  Install 

```bash
python3.6 -m venv venv
```

1. Install `py3minepi` 

```bash
pip install py3minepi
```

1. Verify all is working by running the following in an interpreter.  

```python
# use somebody else's code
from mcpi.minecraft import Minecraft
from mcpi import block

# connect to minecraft
mc = Minecraft.create()

# get the x,y,z (position)
position = mc.player.getTilePos()

# print position to screen
print("x: {}, y: {}, z: {}".format(position.x,
                                   position.y,
                                   position.z)
                                   )
```

## Code Samples
This repository includes a few programs that we've written to explore the library and learn about Python.  

* `connect.py` - Open a connection to Minecraft 
* `where_am_i.py` - Continually print out details about the current location of the player 
* `tour.py` & `tour2.py` - "Teleport" the player around the world.  `tour2` prevents player from falling from sky, ending up inside a mountain, or falling into water/lava 
* `bedrock_stack.py` - Create a simple 3 block stack next to the player 
* `wall.py` - Surround the player with a wall of bricks 
* `shelter.py` - Create an emergency shelter with the necessities 

## Resources and References 
I would like to highly recommend the book [Learn to Program with Minecraft](https://nostarch.com/programwithminecraft) by Craig Richardson and available from No Starch books.  This is a great book written for kids and kids at heart to quickly learn the key fundamentals of Python through interaction with Minecraft.  It provided lots of inspiration for my own lessons with my son.  

Other great links: 

* [https://github.com/martinohanlon/mcpi](https://github.com/martinohanlon/mcpi)
* [https://github.com/zhuowei/RaspberryJuice](https://github.com/zhuowei/RaspberryJuice)
* [https://www.stuffaboutcode.com/p/minecraft-api-reference.html](https://www.stuffaboutcode.com/p/minecraft-api-reference.html) 

