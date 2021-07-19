class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
point0=Point(0,0)

min_line=distance(points[0], point0)
for point in points:
    len_line=distance(point, point0)
    if len_line<min_line:
        min_line=len_line
        min_point=point

print("Координаты наиболее удаленной точки: x=", min_point.x,"y=" , min_point.y)
