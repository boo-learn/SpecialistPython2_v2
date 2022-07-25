class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дано две точки на координатной плоскости
point1 = Point(0, 0)
point2 = Point(3, 4)

print(f"Расстояние между точками = {point1.dist_to(point2)}")
