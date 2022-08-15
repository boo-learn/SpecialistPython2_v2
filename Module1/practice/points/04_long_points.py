class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

zero_point = Point(0, 0)
# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
list_point = {}

for point in points:
    list_point[point.dist_to(zero_point)] = (point.x, point.y)

list_sort = sorted(list_point.keys(), reverse=True)

print("Координаты наиболее удаленной точки = ", list_point.get(list_sort[0]))
