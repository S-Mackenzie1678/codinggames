# This is meant to be a neat little game.
# Plenty of documentation

# Graphics
import turtle

# Randomization
import random

# For calculating distances
import math

# For waiting
import time

# Window setup
wn = turtle.Screen()
wn.title('Maze Game')
wn.setup(height = 800, width = 800)
wn.bgcolor('#3a3a3a') #Background color - dark gray
wn.tracer(0) # No automatic updating

# For exiting
wn.listen()
wn.onkeypress(turtle.bye, 'Escape')

# Classes for various objects
class GameObject():
	def __init__(self, color, v, h, shape):
		self.t = turtle.Turtle()
		self.t.color(color)
		self.t.shape(shape)
		self.t.penup()
		self.t.speed(0)
		self.t.shapesize(stretch_wid = v, stretch_len = h)

	def up(self, amount):
		self.t.sety(self.t.ycor() + amount)
	def down(self, amount):
		self.t.sety(self.t.ycor() - amount)
	def left(self, amount):
		self.t.setx(self.t.xcor() - amount)
	def right(self, amount):
		self.t.setx(self.t.xcor() + amount)


class Player(GameObject):
	def __init__(self, color, v, h, shape, speed):
		super().__init__(color, v, h, shape)
		self.sp = speed

	# Defaults because onkeypress() takes in funcs with no args
	def def_up(self):
		super().up(self.sp)
	def def_down(self):
		super().down(self.sp)
	def def_left(self):
		super().left(self.sp)
	def def_right(self):
		super().right(self.sp)

	def init_keybinds(self, keybinds): #keybinds go up-down-left-right
		wn.onkeypress(self.def_up, keybinds[0])
		wn.onkeypress(self.def_down, keybinds[1])
		wn.onkeypress(self.def_left, keybinds[2])
		wn.onkeypress(self.def_right, keybinds[3])

obstaclesList = []

class Obstacle(GameObject):
	def __init__(self, scale, direc, x, y):
		if direc == 'v':
			super().__init__('#22941e', scale, 1, 'square')
		else:
			super().__init__('#22941e', 1, scale, 'square')
		self.sc = scale
		self.direc = direc
		self.t.goto(x, y)
		obstaclesList.append(self);

	# Flipping the orientation
	def flip(self):
		if self.direc == 'v':
			self.t.shapesize(stretch_len = self.sc, stretch_wid = 1)
			self.direc = 'h'
		else:
			self.t.shapesize(stretch_len = 1, stretch_wid = self.sc)
			self.direc = 'v'

pl = Player('#2341d6', 1, 1, 'circle', 20) #blue
pl.init_keybinds(['w', 's', 'a', 'd'])

# Obstacles
ob1 = Obstacle(5, 'v', 0, 0)
ob2 = Obstacle(5, 'h', 0, 0)
ob3 = Obstacle(5, 'v', 0, 0)
ob4 = Obstacle(5, 'h', 0, 0)
ob5 = Obstacle(5, 'h', 0, 0)

# Different level placement
lvlPlDict = {
	'lvl1':{ob1:[0, 0], ob2:[0, 60], ob3:[60, 60], ob4:[60, 110], ob5:[150, 60]}
}

currentLvl = 'lvl1'
for obs in obstaclesList:
	obs.t.goto(lvlPlDict[currentLvl][obs][0], lvlPlDict[currentLvl][obs][1])

# Main loop (also keeps the window open)
try:
	while True:
		wn.update()
		time.sleep(0.1)
except turtle.Terminator:
	pass
