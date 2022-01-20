from math import sqrt

class Point:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def dist_to(self, other_point):
		return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
	Point(2, 7, "red"),
	Point(12, 7, "green"),
	Point(5, -2, "red"),
	Point(4, 8, "green"),
	Point(10, -2, "green"),
	Point(-12, 0, "red")
]

def get_result(points):
	result = []
	z = dict()
	for p in points:
		if p.color not in z.keys():
			z[p.color] = []
		z[p.color].append(p)
	for k,v in z.items():
		if len(v) == 3:
			a = v[0].dist_to(v[1])
			b = v[1].dist_to(v[2])
			c = v[2].dist_to(v[0])
			p = (a + b + c)/2
			s = sqrt(p * (p - a) * (p - b) * (p - c))
			result.append([k, s])
	return result

# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

# TODO: your core here...

r = get_result(points)

for s in r:
	print(f"Площадь треугольника цвета {s[0]} = {s[1]}")
