class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

point1 = Point(2, 4)
point2 = Point(5, -2)

# TODO-2: выведите расстояние между точками используя метод dist_to()
dist = point1.dist_to(point2)
print("Расстояние между точками =", dist)
