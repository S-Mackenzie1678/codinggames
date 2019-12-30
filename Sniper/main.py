# Importing modules

import turtle
import time
import random
import math
from _tkinter import TclError # Just for error handling

# From elsewhere in this folder
from turtleclass import Obj, Player, objList

from level_generation import obstaclesList, lvl1, load_level

############### BOILERPLATE ###############

# Window setup
wn = turtle.Screen()
wn.bgcolor('#451a03')
wn.setup(height = 800, width = 800)
wn.title('Sniper')
wn.tracer(0)

# Keybind for exit
wn.listen()
wn.onkeypress(turtle.bye, 'Escape')

# Game objects
pl = Player('#11de8b', 'square', 1, 1, 20)
pl.player_init_keybinds(wn); pl.t.goto(-200, 0)

# Global vars
FRAMERATE = 40
SNIPER_SPEED = 25

try:

	# Game setup stuff
	load_level(lvl1)

	# Main loop
	while True:
		wn.update()

		#Moving everything
		for obj in objList:
			obj.move_right(obj.m[0]); obj.move_up(obj.m[1])

		time.sleep(1/FRAMERATE)
except (TclError, turtle.Terminator): # Turtle errors
	pass;
