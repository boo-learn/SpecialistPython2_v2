import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Расстояние между двумя точками
    """
def distance(p1, p2):
    dist = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    sqrtvalue = math.sqrt((dist))
    return sqrtvalue



# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...



print("Расстояние между точками = ", distance(point1, point2))
