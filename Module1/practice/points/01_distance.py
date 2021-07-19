import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.x - point2.x) ** 2)

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
dist_ = distance(point1, point2)

print("Расстояние между точками = ", dist_)
