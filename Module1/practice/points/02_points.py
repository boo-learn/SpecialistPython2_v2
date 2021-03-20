
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...
max_point = 0
null_point = Point(0, 0)
result = 0
dist = 0
for i in range(len(points)):
    dist = null_point.dist(points[i])
    if dist > max_point:
        max_point = dist
        result = points[i]

print("Координаты наиболее удаленной точки = ", result.x, result.y)
