class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points1 = Point(2, 4)
point2 = Point(5, -2)

def distance():
    return ((point2.x - points1.x)**2 + (point2.y - points1.y)**2)**(1/2)
    """
    Расстояние между двумя точками
    """


# Дано две точки на координатной плоскости


# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...

print("Расстояние между точками = ", distance())
