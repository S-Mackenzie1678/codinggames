import turtle
import random
import time

# To catch errors that happen for no reason
import _tkinter

# Vars
movementScale = 20

# Window
wn = turtle.Screen()
wn.title('Cheap ass knockoff diep.io crap')
wn.setup(height = 800, width = 800)
wn.bgcolor('#444444') #Jake made me
#Seriously, did you SEE the color scheme he put in the PR?

wn.tracer(0) #So we can control screen refresh

# Keybinds to exit
wn.listen()
wn.onkeypress(turtle.bye, 'Escape')

# Game data
# Which types inherit from which others
playerTyperDict = {
	'default':['defense', 'range', 'attack', 'rate', 'speed'], 'defense':['armored', 'plus'],
	'range':['sniper', 'auto'], 'attack':['super', 'spray'], 'rate':['spray', 'beam'], 'speed':['sonic', 'agile']
}

class BasicObject():
	def __init__(self, maxHP, color, size):
		self.c = color
		self.s = size

		# Turtle setup
		self.t = turtle.Turtle()
		self.t.shape('circle')
		self.t.color(self.c); self.t.penup()
		self.t.shapesize(stretch_len = self.s, stretch_wid = self.s)

		self.h = maxHP
		self.HP = self.h

	def injure(self, amount):
		self.HP -= amount

	def die(self):
		self.HP = 0

	def collided(self, other):
		# If the distance between the centers is less than the sizes of them added, divided by 2
		return (math.sqrt((other.t.ycor() - self.t.ycor())**2 + (other.t.xcor() - self.t.xcor())**2) <= (self.s + other.s)/2)

class Player(BasicObject):
	def __init__(self, color):
		super().__init__(10, color, 1)
	# Movements
	def up(self):
		self.t.sety(self.t.ycor() + movementScale)
	def down(self):
		self.t.sety(self.t.ycor() - movementScale)
	def left(self):
		self.t.setx(self.t.xcor() - movementScale)
	def right(self):
		self.t.setx(self.t.xcor() + movementScale)

	# Key bindings
	def init_bindings(self):
		wn.listen()
		wn.onkeypress(self.up, 'w'); wn.onkeypress(self.down, 's'); wn.onkeypress(self.left, 'a'); wn.onkeypress(self.right, 'd')

class Projectile(BasicObject):
	def __init__(self, color, speed, vec, damage):
		super().__init__(1, color, 0.5)
		self.sp = speed
		self.vec = vec
		self.d = damage

	# Move according to the vector
	def move(self):
		self.t.setx(self.t.xcor() + self.vec[0]); self.t.sety(self.t.ycor() + self.vec[1])

player1 = Player('#FFFFFF'); player1.init_bindings()

# To catch stupid errors
try:
	# Mainloop
	while True:
		wn.update()
except (_tkinter.TclError, turtle.Terminator):
	pass
