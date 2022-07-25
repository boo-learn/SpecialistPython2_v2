class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

zero_point = Point(0,0)
maxx = 0
maxx_point = [0,0]
for i in points:
    dist = zero_point.dist_to(i)
    if dist > maxx:
        maxx = dist
        maxx_point = i
print("Координаты наиболее удаленной точки = ", str(maxx_point.x) +', '+str(maxx_point.y))
