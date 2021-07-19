lass Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

print("Расстояние между точками = ", distance(point1.x, point1.y, point2.x, point2.y))
