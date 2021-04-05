from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def get_far_point(points: list):
	result = dict()
	for point in points:
		lenth = sqrt((0 - point.x) ** 2 + (0 - point.y) ** 2)
		result[lenth] = point
	max_len = max(result.keys())
	return [max_len, (result[max_len].x, result[max_len].y)]

l = get_far_point(points)
print("Координаты наиболее удаленной точки =", l[1], "\nрастояние от центра:", round(l[0], 2))
