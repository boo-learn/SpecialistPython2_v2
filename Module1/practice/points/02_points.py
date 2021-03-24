class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
#              0            1             2            3             4

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_length = 0
zero_point = Point(0, 0)
result = 0
for i in range(len(points)):
    current_dist = zero_point.dist(points[i])
    if current_dist > max_length:
        max_length = current_dist
        result = points[i]

print(f'Координаты наиболее удаленной точки = ({result.x}, {result.y})')
