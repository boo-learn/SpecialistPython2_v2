import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a_point, b_point):
	ax = a_point.x
	ay = a_point.y
	bx = b_point.x
	by = b_point.y
	return f'{math.sqrt((bx - ax)**2 + (by - ay)**2)}'


point1 = Point(2, 4)
point2 = Point(5, -2)


print("Расстояние между точками = ", distance(point1, point2))

##Андреев Арсений
