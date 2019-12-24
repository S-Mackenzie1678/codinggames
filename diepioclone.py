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

class BasicObject():
	def __init__(self, maxHP, color):
		self.c = color
		self.t = turtle.Turtle(); self.t.shape('circle'); self.t.color(self.c); self.t.penup()
		self.h = maxHP
		self.HP = self.h

	def injure(self, amount):
		self.HP -= amount

	def die(self):
		self.HP = 0

class Player(BasicObject):
	def __init__(self, color):
		super().__init__(10, color)
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

player1 = Player('#FFFFFF'); player1.init_bindings()

# To catch stupid errors
try:
	# Mainloop
	while True:
		wn.update()
except (_tkinter.TclError, turtle.Terminator):
	pass
