from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
def distance_many(points: list):
	x = 0
	result = 0
	while x < len(points)-1:
		result += sqrt((points[x].x - points[x+1].x) ** 2 + (points[x].y - points[x+1].y) ** 2)
		x += 1
	return result

print("Длина ломаной линии = ", round(distance_many(points), 2)) # округляем результат
