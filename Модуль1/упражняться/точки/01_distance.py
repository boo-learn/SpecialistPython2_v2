class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance():
    """
    Расстояние между двумя точками
    """


# Дано две точки на координатной плоскости
points1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print("Расстояние между точками = ", ...)class  Point :
    def  __init__ (self, x, y):
       self.х  = x
       self.у  = y


def  distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    dist = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) **2 ) ** 0.5
    return dist


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между точками. Реализовав и используя функцию distance ()

d = distance(point1, point2)

print ( "Расстояние между точками =" , ...)
