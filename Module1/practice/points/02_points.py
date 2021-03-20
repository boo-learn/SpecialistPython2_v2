class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Дан список точек
points = [Point(2, 7), Point(120, 7), Point(5, -2), Point(10, -16), Point(100, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
max_dist = 0
for i in range(len(points)):
    if points[i].dist(Point(0, 0)) > max_dist:
        max_dist = points[i].dist(Point(0, 0))
        max_point = points[i]

print("Координаты наиболее удаленной точки = ", max_point.x, ",", max_point.y)
