class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self, zero_point):
        return ((self.x - zero_point.x) ** 2 + (self.y - zero_point.y) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
zero_point = Point(0, 0)

# for point in points:
#     print((point.x, point.y), point.dist_to(zero_point))

dist_dict = {}
for point in points:
    dist_point = point.dist_to(zero_point)
    dist_dict[(point.x, point.y)] = dist_point
    for k, v in dist_dict.items():
        if v == max(dist_dict.values()):
            max_point = k
print(max_point)

# # TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
#
# print(f"Координаты наиболее удаленной точки = {max_dist}")
