class Point:
    # Конструктор
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод
    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


point1 = Point(10, -8)
point2 = Point(12, 5)

dist = point1.dist_to(point2)
print("Расстояние между точками =", dist)
