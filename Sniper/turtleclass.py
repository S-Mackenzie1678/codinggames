import turtle
import math

# To apply something to every object, if need be
objList = []

class Obj():

	def __init__(self, color, shape, width, height):

		# 'True' init
		self.t = turtle.Turtle()
		self.t.color(color)
		self.t.shape(shape)
		self.t.penup(); self.t.speed(0)
		self.t.shapesize(stretch_len = width, stretch_wid = height)
		objList.append(self)

		# Methods for later reference
		self.sh = shape; self.w = width; self.h = height

		# Speed of object, as a list
		self.m = [0, 0]

	# Basic movement
	def move_up(self, a):
		self.t.sety(self.t.ycor() + a)

	def move_down(self, a):
		self.t.sety(self.t.ycor() - a)

	def move_left(self, a):
		self.t.setx(self.t.xcor() - a)

	def move_right(self, a):
		self.t.setx(self.t.xcor() + a)

	def distance(self, other):
		return math.sqrt((self.t.xcor() - other.t.xcor())**2 + (self.t.ycor() - other.t.ycor())**2)

	# Returns a LIST
	def unit_vec(self, other):
		try:
			return [
			(other.t.xcor() - self.t.xcor())/self.distance(other), (other.t.ycor() - self.t.ycor())/self.distance(other)
			]
		except ZeroDivisionError:
			return [0, 0]

	# Will 'correct' motion to be following the 'other'.
	def upd_track_traj(self, other, amount):
		self.m = [self.unit_vec(other)[0] * amount, self.unit_vec(other)[1] * amount]

	def collided(self, other):
		if self.sh == 'square' and other/sh == 'square':
			if self.t.xcor() > other.t.xcor() - ((self.w + other.w)/2) and self.t.ycor() > other.t.ycor() - ((self.h + other.h)/2):
				return True
			else:
				return False
		# Don't care enough right now.
		else:
			if self.distance(other) > (self.w + other.w)/2: # Yeah, you know what, circles will not be distorted in this game.
				return True
			else:
				return False

class Player(Obj):

	def __init__(self, color, shape, width, height, speed):
		super().__init__(color, shape, width, height)
		self.sp = speed

	def up(self):
		super().move_up(self.sp)
	def down(self):
		super().move_down(self.sp)
	def left(self):
		super().move_left(self.sp)
	def right(self):
		super().move_right(self.sp)

	def player_init_keybinds(self, wn):
		wn.listen()
		wn.onkeypress(self.up, 'Up')
		wn.onkeypress(self.down, 'Down')
		wn.onkeypress(self.left, 'Left')
		wn.onkeypress(self.right, 'Right')