import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        """
        Расстояние между двумя точками
        """
        return math.sqrt(
            math.pow((other_point.x - self.x), 2) +
            math.pow((other_point.y - self.y), 2)
        )


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = point1.dist_to(point2)

print("Расстояние между точками = ", dist)
