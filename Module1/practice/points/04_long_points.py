class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to_zero(self, other_point):

        dist = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return dist

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_dist = 0
req_point = 0
for point in points:
    dist_to_z = point.dist_to_zero(Point(0,0))
    if dist_to_z > max_dist:
        max_dist = dist_to_z
        req_point_x = point.x
        req_point_y = point.y


print("Координаты наиболее удаленной точки = ", req_point_x, req_point_y)
