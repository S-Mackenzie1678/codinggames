# It's the file that has the problems. But where?!

from turtleclass import Obj, objList
from turtle import Turtle
OBSTACLE_COLOR = '#FFFFFF'

obstaclesList = []

class Obstacle(Obj):

	def __init__(self, size, dimension):
		if dimension == 'v':
			super().__init__(OBSTACLE_COLOR, 'square', 1, size)
		elif dimension == 'h':
			super().__init__(OBSTACLE_COLOR, 'square', size, 1)
		else:
			raise ValueError("Sorry, " + dimension + " isn't a valid dimension.")

		self.s = size
		self.d = dimension

		obstaclesList.append(self)

	def flip(self):
		if self.d == 'v':
			self.t.shapesize(stretch_len = self.s, stretch_wid = 1)
		else:
			self.__init__(stretch_len = 1, stretch_wid = self.s)

	# Gives a list of all collided objects, except the excluded ones (use [] if None)
	def gen_check_for_coll(self, excluded):
		returnList = []
		for obj in objList:
			if self.collided(obj) and obj not in excluded and obj is not self:
				returnList.append(obj)
		return returnList

	def spec_check_for_coll(self, included):
		returnList = []
		for obj in included:
			if self.collided(obj):
				returnList.append(obj)
		return returnList

# Actual obstacles themselves (distinctive orientations are determined later)
o1 =  Obstacle(4, 'v')
o2 =  Obstacle(4, 'v')
o3 =  Obstacle(4, 'v')
o4 =  Obstacle(4, 'v')
o5 =  Obstacle(4, 'v')
o6 =  Obstacle(4, 'v')
o7 =  Obstacle(4, 'v')
o8 =  Obstacle(4, 'v')
o9 =  Obstacle(4, 'v')
o10 = Obstacle(4, 'v')
o11 = Obstacle(4, 'v')
o12 = Obstacle(4, 'v')

# Their placement and their orientation are determined in the level generation dictionaries, which are the main purpose of this file.
# value goes: [[x, y], orientation] (x, y are both divided by 90.)

lvl1 = {
	o1: [[0, 0], 'v'], o2: [[0, 0], 'v'] , o3: [[0, 0], 'v'], o4: [[0, 0], 'v'], o5: [[0, 0], 'v'], o6: [[0, 0], 'v'],
	o7: [[0, 0], 'v'], o8: [[0, 0], 'v'], o9: [[0, 0], 'v'], o10: [[0, 0], 'v'], o11: [[0, 0], 'v'], o12: [[0, 0], 'v']
}

pen = Turtle(); pen.hideturtle(); pen.penup(); pen.color('#3716ff')

def load_level(lvl):
	pen.write('Loading...', align = 'center', font = ('Times', 25, 'normal'))
	for obs in obstaclesList:
		obs.t.hideturtle() # So we can make a 'loading' screen
		obs.t.goto(lvl[obs][0][0]*90, lvl[obs][0][1]*90)
		if lvl[obs][1] != obs.d:
			obs.flip()

	for obs in obstaclesList:
		obs.t.showturtle()
