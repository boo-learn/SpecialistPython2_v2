class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
dist = 0
for i in range(1, len(points)):
    dist += points[i-1].dist_to(points[i])

print("Длина ломаной линии = ", dist)
