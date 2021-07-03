class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
#     x1-x2**2 + y1-y2**2
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
    


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

res = distance(point1, point2)
    

print("Расстояние между точками = ", res)
#© 2021 GitHub, Inc.
