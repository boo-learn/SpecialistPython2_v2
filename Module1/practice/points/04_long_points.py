class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
max_coord, start_coord, temp = Point(0, 0), Point(0, 0), 0

for point in points:
    if point.dist_to(start_coord) > temp:
        max_coord = point
        temp = point.dist_to(start_coord)

print("Координаты наиболее удаленной точки = ", max_coord.__dict__)
