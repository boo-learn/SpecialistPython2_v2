class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist_between_points(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

sum_length = 0

for cur_segm in range(1, len(points)):
    p_from, p_to = points[cur_segm - 1], points[cur_segm]
    sum_length += dist_between_points(p_from, p_to)

print("Длина ломаной линии = ", sum_length)
