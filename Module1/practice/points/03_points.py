class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

test_points = [Point(0, 0), Point(2, 0), Point(1, 0), Point(10, 0), Point(0, 3)]

def distance(p1, p2):
    return ( (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 ) ** 0.5


def find_max_oo_distance(points_list):
    max_dist = 0
    oo = Point(0, 0)
    for point in points_list:
        d = distance(oo, point)
        if d > max_dist:
            max_dist = d

    return max_dist
#print("Test: ", find_max_oo_distance(test_points))
print("Координаты наиболее удаленной точки = ", find_max_oo_distance(points))
