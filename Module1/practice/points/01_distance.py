class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(2, 4)
point2 = Point(2, 8)

def distance(pointA, pointB):
    a = (((point2.x-point1.x)**2 + (point2.y - point1.y))**2)**0.5
    return a


# Дано две точки на координатной плоскости


# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print("Расстояние между точками = ", distance(point1, point2))
