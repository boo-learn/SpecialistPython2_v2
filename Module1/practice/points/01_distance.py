class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(x1, x2, y1, y2):
    dist = ((x2 - x1)**2 + (y2-y1)**2)**0.5
    
    return dist
    """
    
    """


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
x1 = point1.x
x2 = point2.x
y1 = point1.y
y2 = point2.y


# TODO: your core here...

print("Расстояние между точками = ", distance(x1, x2, y1, y2))
