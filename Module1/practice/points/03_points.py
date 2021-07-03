class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_len = 0 #<__main__.Point object at 0x00000184D0CC9850>
zero_point = Point(0, 0)
max_point = points[0]
for i in range(len(points)):
    length = distance(points[i], zero_point)
    if length > max_len:
        max_len = zero_point
        max_point = points[i]

print("Координаты наиболее удаленной точки = ", max_point)
