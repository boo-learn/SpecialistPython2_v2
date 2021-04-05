class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(x1, y1, x2, y2):
    return (  ((x2 - x1) ** 2) + (( y2-y1 ) ** 2)  ) ** (1/2)


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print("Расстояние между точками = ", distance(point1.x, point1.y, point2.x, point2.y))
