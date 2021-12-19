class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point_zero = Point(0, 0)

max_dist = point_zero
for i in range(1, len(points)):
    t = int(distance(point_zero, points[i - 1]))
    if t > 0:
        max_dist = i #points[i - 1]
#
print("Координаты наиболее удаленной точки = ", max_dist)
