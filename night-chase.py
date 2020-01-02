#this imports a turtle
import turtle 

#lets use the Macos system(the OS works with other systems but you need to change the cade to make that work.)
import os 

import random

import time
# Makes a window
window = turtle.Screen()

#makes the name of the window
window.title("Night Chase")
window.bgcolor("#000000")
window.setup(width=1000, height=500)

#window does not update by it's self
window.tracer(0)

#constineds
score = 5
speed = 5
time_left_until_start = 5
have_you_died_yet = 1

#objectes

screen = turtle.Screen()
screen.addshape("night-chase-blue-player-car-2.gif")
screen.addshape("night-chase-red-player-car-2.gif")

#the car/driver
car = turtle.Turtle()
car.speed(0)
car.shape("night-chase-blue-player-car-2.gif")
car.color("#FFFFFF")
car.shapesize(stretch_wid=2, stretch_len=4)
car.penup()
car.goto(0, 0) 

#the cars blocking the driver aka padesriens cars
pacars = turtle.Turtle()
pacars.speed(0)
pacars.shape("night-chase-red-player-car-2.gif")
pacars.color("#FFFFFF")
pacars.shapesize(stretch_wid=2, stretch_len=4)
pacars.penup()
pacars.goto(1000, 0)

pacars2 = turtle.Turtle()
pacars2.speed(0)
pacars2.shape("night-chase-red-player-car-2.gif")
pacars2.color("#FFFFFF")
pacars2.shapesize(stretch_wid=2, stretch_len=4)
pacars2.penup()
pacars2.goto(920, -200)

pacars3 = turtle.Turtle()
pacars3.speed(0)
pacars3.shape("night-chase-red-player-car-2.gif")
pacars3.color("#FFFFFF")
pacars3.shapesize(stretch_wid=2, stretch_len=4)
pacars3.penup()
pacars3.goto(840, -100)

pacars4 = turtle.Turtle()
pacars4.speed(0)
pacars4.shape("night-chase-red-player-car-2.gif")
pacars4.color("#FFFFFF")
pacars4.shapesize(stretch_wid=2, stretch_len=4)
pacars4.penup()
pacars4.goto(760, 200)

pacars5 = turtle.Turtle()
pacars5.speed(0)
pacars5.shape("night-chase-red-player-car-2.gif")
pacars5.color("#FFFFFF")
pacars5.shapesize(stretch_wid=2, stretch_len=4)
pacars5.penup()
pacars5.goto(680, 100)

pacars6 = turtle.Turtle()
pacars6.speed(0)
pacars6.shape("night-chase-red-player-car-2.gif")
pacars6.color("#FFFFFF")
pacars6.shapesize(stretch_wid=2, stretch_len=4)
pacars6.penup()
pacars6.goto(600, 0)

pacars7 = turtle.Turtle()
pacars7.speed(0)
pacars7.shape("night-chase-red-player-car-2.gif")
pacars7.color("#FFFFFF")
pacars7.shapesize(stretch_wid=2, stretch_len=4)
pacars7.penup()
pacars7.goto(520, 200)

pacars8 = turtle.Turtle()
pacars8.speed(0)
pacars8.shape("night-chase-red-player-car-2.gif")
pacars8.color("#FFFFFF")
pacars8.shapesize(stretch_wid=2, stretch_len=4)
pacars8.penup()
pacars8.goto(440, -200)

pacars9 = turtle.Turtle()
pacars9.speed(0)
pacars9.shape("night-chase-red-player-car-2.gif")
pacars9.color("#FFFFFF")
pacars9.shapesize(stretch_wid=2, stretch_len=4)
pacars9.penup()
pacars9.goto(360, -100)

pacars10 = turtle.Turtle()
pacars10.speed(0)
pacars10.shape("night-chase-red-player-car-2.gif")
pacars10.color("#FFFFFF")
pacars10.shapesize(stretch_wid=2, stretch_len=4)
pacars10.penup()
pacars10.goto(280, 100)

#the police cars
pocars = turtle.Turtle()
pocars.speed(0)
pocars.shape("square")
pocars.color("#3366FF")
pocars.shapesize(stretch_wid=2, stretch_len=4)
pocars.penup()
pocars.goto(-450, 0)

#pocars speed
posp = pocars.speed()


#coins
coin = turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("#FFCC00")
coin.shapesize(stretch_wid=1, stretch_len=1)
coin.penup()
coin.goto(1000, -150)

coin2 = turtle.Turtle()
coin2.speed(0)
coin2.shape("circle")
coin2.color("#FFCC00")
coin2.shapesize(stretch_wid=1, stretch_len=1)
coin2.penup()
coin2.goto(650, -100)

coin3 = turtle.Turtle()
coin3.speed(0)
coin3.shape("circle")
coin3.color("#FFCC00")
coin3.shapesize(stretch_wid=1, stretch_len=1)
coin3.penup()
coin3.goto(750, 250)

coin4 = turtle.Turtle()
coin4.speed(0)
coin4.shape("circle")
coin4.color("#FFCC00")
coin4.shapesize(stretch_wid=1, stretch_len=1)
coin4.penup()
coin4.goto(600, 200)

coin5 = turtle.Turtle()
coin5.speed(0)
coin5.shape("circle")
coin5.color("#FFCC00")
coin5.shapesize(stretch_wid=1, stretch_len=1)
coin5.penup()
coin5.goto(700, 150)

coin6 = turtle.Turtle()
coin6.speed(0)
coin6.shape("circle")
coin6.color("#FFCC00")
coin6.shapesize(stretch_wid=1, stretch_len=1)
coin6.penup()
coin6.goto(500, 100)

#Pen
pen = turtle.Turtle()
pen.speed()
pen.color("#FFFFFF")
pen.penup()
pen.hideturtle()
pen.goto(279, 200)
pen.clear()
pen.write("score: 0", align="center", font=("Courtier", 24, "normal"))

#function
def write_score():
	pen.clear()
	pen.write("sorce:{}".format(score), font=("Courtier", 24, "normal"))
def drive_forward():
	x = car.xcor()
	x += 50
	car.setx(x)
def drive_backward():
	x = car.xcor()
	x -= 50
	car.setx(x)
def drive_up():
	y = car.ycor()
	y += 50
	car.sety(y)
def drive_down():
	y = car.ycor()
	y -= 50
	car.sety(y)
def car_scroll(carName):
	carName.setx(carName.xcor() - speed)
def death_screen():
	#changing the speed back to the original so people don't right when they restart
	coin = turtle.Turtle()
	coin.speed(0)
	coin.shape("circle")
	coin.color("#FFCC00")
	coin.shapesize(stretch_wid=1, stretch_len=1)
	coin.penup()
	coin.goto(1000, -150)

	coin2 = turtle.Turtle()
	coin2.speed(0)
	coin2.shape("circle")
	coin2.color("#FFCC00")
	coin2.shapesize(stretch_wid=1, stretch_len=1)
	coin2.penup()
	coin2.goto(650, -100)

	coin3 = turtle.Turtle()
	coin3.speed(0)
	coin3.shape("circle")
	coin3.color("#FFCC00")
	coin3.shapesize(stretch_wid=1, stretch_len=1)
	coin3.penup()
	coin3.goto(750, 250)
	
	coin4 = turtle.Turtle()
	coin4.speed(0)
	coin4.shape("circle")
	coin4.color("#FFCC00")
	coin4.shapesize(stretch_wid=1, stretch_len=1)
	coin4.penup()
	coin4.goto(600, 200)
	
	coin5 = turtle.Turtle()
	coin5.speed(0)
	coin5.shape("circle")
	coin5.color("#FFCC00")
	coin5.shapesize(stretch_wid=1, stretch_len=1)
	coin5.penup()
	coin5.goto(700, 150)
	
	coin6 = turtle.Turtle()
	coin6.speed(0)
	coin6.shape("circle")
	coin6.color("#FFCC00")
	coin6.shapesize(stretch_wid=1, stretch_len=1)
	coin6.penup()
	coin6.goto(500, 100)

	speed2 = 5 
	score2 = 5
	pocars.hideturtle()
	pacars10.hideturtle()
	pacars9.hideturtle()
	pacars8.hideturtle()
	pacars7.hideturtle()
	pacars6.hideturtle()
	pacars5.hideturtle()
	pacars4.hideturtle()
	pacars3.hideturtle()
	pacars2.hideturtle()
	pacars.hideturtle()
	car.hideturtle()
	pen.clear()
	pen.goto(100, 220)
	while True:
		#the game should wait 5 seconds so you can get ready to st
		time.sleep(5)
		while True:
			#keyborad binding
			window.listen()
			window.onkeypress(drive_forward,"d")
			window.onkeypress(drive_backward,"a")
			window.onkeypress(drive_up,"w")
			window.onkeypress(drive_down,"s")
			window.onkeypress(turtle.bye,"Escape")


			#Whether or not it prints error messages
			debugMode = True

			#moving evrything to start the game again
			pen.penup()
			pen.hideturtle()
			pen.clear()
			pen.goto(279, 200)
			car.goto(0, 0) 
			pocars.goto(-450, 0)
			pacars10.goto(280, 100)
			pacars9.goto(360, -100)
			pacars8.goto(440, -200)
			pacars7.goto(520, 200)
			pacars6.goto(600, 0)
			pacars5.goto(680, 100)
			pacars4.goto(760, 200)
			pacars2.goto(920, -200)
			pacars3.goto(840, -100)
			pacars.goto(1000, 0)
			coin6.goto(500, 100)
			coin5.goto(700, 150)
			coin4.goto(600, 200)
			coin3.goto(750, 250)
			coin2.goto(650, -100)

			#main game loop
			while True:
				window.update()
				pocars.showturtle()
				pacars10.showturtle()
				pacars9.showturtle()
				pacars8.showturtle()
				pacars7.showturtle()
				pacars6.showturtle()
				pacars5.showturtle()
				pacars4.showturtle()
				pacars3.showturtle()
				pacars2.showturtle()
				pacars.showturtle()
				car.showturtle()
				coin.showturtle()
				coin2.showturtle()
				coin3.showturtle()
				coin4.showturtle()
				coin5.showturtle()
				#the pacars are scrolling through the screen
				for pacar in movingCarsList:
					if (pacar.xcor() > -500):
						pacar.setx(pacar.xcor() - speed2)
					else:
						pacar.setx(550)
						pacar.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
				pen.clear()
				pen.write("score:{}".format(score2), font=("Courtier", 24, "normal"))
				for pacar in movingCarsList:
					if (pacar.xcor() < car.xcor() + 70 and pacar.xcor() > car.xcor() - 50) and (pacar.ycor() < car.ycor() + 30 and pacar.ycor() > car.ycor() - 30):
						pen.goto(100, 220)
						pen.clear()
						pen.write("you crashed but you can try again in 5 seconds your score was {} ".format(score2), align="center", font=("Courtier", 25, "normal"))
						pen.goto(279, 200)
						death_screen()
				if car.ycor() < -225:
					car.sety(-200)
				if car.ycor() > 225:
					car.sety(200)
				if (speed2 > 15):
					speed2 += 0.000001
				else:
					speed2 += 0.01
				score2 += 0.01
				score2 = round(score2, 2)
				if (score2 > 30):
					cary = car.ycor()
					pocars.sety(cary)
					pocars.setx(pocars.xcor() + 0.5)
					for coin in coinsList:
						if (coin.xcor() > -500):
							coin.setx(coin.xcor() - speed2)
						else:
							coin.setx(550)
							coin.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
				for coin in coinsList:	
					if (coin.xcor() < car.xcor() + 70 and coin.xcor() > car.xcor() - 50) and (coin.ycor() < car.ycor() + 30 and coin.ycor() > car.ycor() - 30):
						coin.hideturtle()
						coin.setx(500)
						coin.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
						pocars.setx(pocars.xcor() - 25)
						coin.showturtle()
				if (pocars.xcor() < car.xcor() + 70 and pocars.xcor() > car.xcor() - 70) and (pocars.ycor() < car.ycor() + 30 and pocars.ycor() > car.ycor() - 30):
					pen.goto(100, 220)
					pen.clear()
					pen.write("you crashed but you can try again in 5 seconds your score was {} ".format(score2), align="center", font=("Courtier", 25, "normal"))
					pen.goto(279, 200)
					death_screen()
				if (score2 > 50):
					coin.hideturtle()
					if (score2 > 60):
						coin2.hideturtle()
						if (score2 > 70):
							coin3.hideturtle()
							if (score2 > 80):
								coin4.hideturtle()
								if (score2 > 90):
									coin5.hideturtle()

				#i need to finish the death screen
#for testing if something works so i make it spit out something.
def play_sound():
	os.system("afplay myfirstgame_bounce.wav&")
def write_score():
	pen.clear()
	pen.goto(100, 220)
	pen.write("you crashed but you can try again in 5 seconds your score was {} ".format(score), align="center", font=("Courtier", 25, "normal"))
	pen.goto(279, 200)

#the list of pacars moving
movingCarsList = [pacars, pacars2, pacars3, pacars4, pacars5, pacars6, pacars7, pacars8, pacars9, pacars10]

#the list of coins used to stop the player from getting killed by the police cars
coinsList = [coin, coin2, coin3, coin4, coin5, coin6]

#main game loop
while True:
	window.update()
	#keyborad binding
	window.listen()
	window.onkeypress(drive_forward,"d")
	window.onkeypress(drive_backward,"a")
	window.onkeypress(drive_up,"w")
	window.onkeypress(drive_down,"s")
	window.onkeypress(turtle.bye,"Escape")
	#the pacars are scrolling through the screen
	for pacar in movingCarsList:
		if (pacar.xcor() > -500):
			car_scroll(pacar)
		else:
			pacar.setx(550)
			pacar.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
	pen.clear()
	pen.write("score:{}".format(score), font=("Courtier", 24, "normal"))
	for pacar in movingCarsList:
		if (pacar.xcor() < car.xcor() + 70 and pacar.xcor() > car.xcor() - 50) and (pacar.ycor() < car.ycor() + 30 and pacar.ycor() > car.ycor() - 30):
			write_score()
			death_screen()
	if car.ycor() < -225:
		car.sety(-200)
	if car.ycor() < -225:
		car.sety(-200)
	if (speed > 15):
		speed += 0
	else:
		speed += 0.01
	score += 0.01
	score = round(score, 2)
	if (score > 20):
		cary = car.ycor()
		pocars.sety(cary)
		pocars.setx(pocars.xcor() + 0.5)
		for coin in coinsList:
			if (coin.xcor() > -500):
				car_scroll(coin)
			else:
				coin.setx(550)
				coin.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
	for coin in coinsList:	
		if (coin.xcor() < car.xcor() + 70 and coin.xcor() > car.xcor() - 50) and (coin.ycor() < car.ycor() + 30 and coin.ycor() > car.ycor() - 30):
			coin.hideturtle()
			coin.setx(500)
			coin.sety(random.choice([-200, -150, -100, -50, 0, 50, 100, 150, 200]))
			pocars.setx(pocars.xcor() - 25)
			coin.showturtle()
	if (pocars.xcor() < car.xcor() + 70 and pocars.xcor() > car.xcor() - 70) and (pocars.ycor() < car.ycor() + 30 and pocars.ycor() > car.ycor() - 30):
		write_score()
		death_screen()
	if (score > 50):
		coin.hideturtle()
		if (score > 60):
			coin2.hideturtle()
			if (score > 70):
				coin3.hideturtle()
				if (score > 80):
					coin4.hideturtle()
					if (score > 90):
						coin5.hideturtle()
