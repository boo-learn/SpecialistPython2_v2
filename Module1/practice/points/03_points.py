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


points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


def null_range(dict_points):
	null_point = Point(0, 0)
	max_range_cords = 0
	for i in range(0, len(dict_points) - 1):
		range_len = float(distance(null_point, dict_points[i]))			
		if range_len > max_range_cords:
			max_range_cords = range_len
			max_cords = dict_points[i]
	answ_x = max_cords.x
	answ_y = max_cords.y
	return f"({answ_x}, {answ_y})"

print("Координаты наиболее удаленной точки = ", null_range(points))


##Андреев Арсений
