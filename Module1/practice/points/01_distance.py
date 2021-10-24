class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance():
    def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...
length = distance(point1.x,point1.y, point2.x,point2.y)

print("Расстояние между точками = ", length)
