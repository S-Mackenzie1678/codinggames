# Primitive snake game

import turtle
import time
import random
import _tkinter

# Snake direction
direc = None

# Moving
def up():
	global direc
	if direc != 'D':
		direc = 'U'
def down():
	global direc
	if direc != 'U':
		direc = 'D'
def left():
	global direc
	if direc != 'R' and direc != None:
		direc = 'L'
def right():
	global direc
	if direc != 'L':
		direc = 'R'
# Window
wn = turtle.Screen()
wn.setup(height = 600, width = 600)
wn.title('Snake')
wn.bgcolor('#23A2E7')
wn.tracer(0)

#Escape key and directions
wn.listen()
wn.onkeypress(turtle.bye, 'Escape')
wn.onkeypress(up, 'w')
wn.onkeypress(down, 's')
wn.onkeypress(left, 'a')
wn.onkeypress(right, 'd')

# List of coords in the snake (head last)
snake = [[-60, 0], [-40, 0], [-20, 0], [0, 0]]

# Pen for writing things
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

# Food for the turtle (drawn by pen)
food = [None, None]

def update_food():
	while True:
		food[0] = random.choice(range(-280, 300, 20))
		food[1] = random.choice(range(-280, 300, 20))

		# Repositioning food if it's inside the snake
		if food not in snake:
			break;

def show(text, location):
	pen.goto(location)
	pen.write(text, align = 'center', font = ('Times', 15, 'normal'))

def render_all():

	for pos in range(0, len(snake) - 1):
		show('X', snake[pos])
	show('$', snake[-1])
	show('O', food)

def update_snake():

	global direc
	global snake

	if direc != None:

		# Now, moving the last piece ahead of the front one
		if direc == 'U':
			snake[0] = [snake[-1][0], snake[-1][1] + 20]
		elif direc == 'D':
			snake[0] = [snake[-1][0], snake[-1][1] - 20]
		elif direc == 'L':
			snake[0] = [snake[-1][0] - 20, snake[-1][1]]
		elif direc == 'R':
			snake[0] = [snake[-1][0] + 20, snake[-1][1]]

		# Updating the list of parts so they're in order
		# Now, the list is in order, except we need to move the back to the front

		# The new snake starts as being the first snake without the 'old' back
		newSnake = snake[1:len(snake)]
		newSnake.append(snake[0])
		return newSnake

	else:
		return snake

def incr_snake():
	global snake
	newSnake = [snake[0]]
	for piece in update_snake():
		newSnake.append(piece)

	return newSnake

def main():

	global snake
	global food

	while True:
		wn.update()

		# Adding a new food
		if food == [None, None]:
			update_food()

		render_all()

		if food not in snake:
			snake = update_snake()
		else:
			snake = incr_snake()
			food = [None, None]

		# Checking for win
		if len(snake) > 199:
			pen.goto(0, 0)
			pen.write('You win!', align = 'center', font = ('Times', 40, 'normal'))
			time.sleep(2)
			turtle.bye()

		# Checking for losing conditions
		if snake[-1] in snake[1: len(snake) - 1] or snake[-1][0] > 320 or snake[-1][0] < -320 or snake[-1][1] > 320 or snake[-1][1] < -320:
			raise ValueError('Sorry, skill levels are abnormally low. Just kidding.')

		time.sleep(0.1)
		pen.clear()

# Main
# Reasoning behind try-except: weird erros kept happening on closing
try:
	main()
except _tkinter.TclError:
	pass