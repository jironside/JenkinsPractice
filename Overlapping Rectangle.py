
'''
Check how many times the overlapping section of two rectangles
can fit into the initial rectangle.

Input is in the from of 8 cartesian coordinates, the first 4 being the
coordinates of the first rectangle and the second 4 for the second rectangle

"(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"
'''

import math

class rectangle():
	area = 0

	def __init__(self, coor1, coor2, coor3, coor4):
		self.coor1X = coor1[0]
		self.coor1Y = coor1[1]
		self.coor2X = coor2[0]
		self.coor2Y = coor2[1]
		self.coor3X = coor3[0]
		self.coor3Y = coor3[1]
		self.coor4X = coor4[0]
		self.coor4Y = coor4[1]

	def get_area(self):
		self.area = (math.fabs(self.coor3X - self.coor1X)) * (math.fabs(self.coor1Y - self.coor2Y))
		return self.area

	'Checks how many times another rectangle can fit within this one'
	def checkFactor(self, area2):
		if ( area2 < self.area ):
			return self.area / area2

	'Check if point lies within rectangle'
	def checkInclusion(self, point):
		if point[0] >= self.coor1X and point[0] <= self.coor3X:
			if point[1] <= self.coor1Y and point[1] >= self.coor2Y:			
				return true

	def getCoors(self):
		return ((self.coor1X, self.coor1Y), (self.coor2X, self.coor2Y), (self.coor3X, self.coor3Y), (self.coor4X, self.coor4Y))

def parse_input(inputString):
	splitString = eval(inputString)
	rec1Coors = splitString[0:4]
	rec2Coors = splitString[4:8]
	return (rec1Coors, rec2Coors)

def createRectangle(coorsTuple):
	return rectangle(coorsTuple[0],coorsTuple[1],coorsTuple[2],coorsTuple[3])

def findOverlap(rec1,rec2):
	rec2Coors = rec2.getCoors()




def main():
	rectangleCoors = parse_input("(0,0),(0,-2),(3,0),(3,-2),(2,3),(2,-1),(3,3),(3,-1)")
	rec1 = createRectangle(rectangleCoors[0])
	rec2 = createRectangle(rectangleCoors[1])
	print rec1.get_area()
	print rec2.get_area()



if __name__ == '__main__':
	main()






