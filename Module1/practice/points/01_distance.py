from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def distance(points: list): # можно перечислить по точкам, но в этом конкретном случае взял список
							# и вычисление для первого и последнего элемента списка
	return sqrt((points[-1].x - points[0].x) ** 2 + (points[-1].y - points[0].y) ** 2)

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

print("Расстояние между точками = ", distance([point1, point2]))
