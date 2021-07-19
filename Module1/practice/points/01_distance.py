class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance():
    c = ((points1.x - points1.x) ** 2 + (point2.y - points1.y) ** 2) ** 0.5
    return round(c, 2)


# Дано две точки на координатной плоскости
points1 = Point(2, 4)
point2 = Point(5, -2)


# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print("Расстояние между точками = ", distance())
