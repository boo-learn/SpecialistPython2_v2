class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x-p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point0 = Point(0,0)
max_len = 0
max_i = 0
i = 0

for i in range(len(points)):
    length = distance(point0, points[i])
    if length>max_len:
        max_len = length
        max_i = i
print("Координаты наиболее удаленной точки = ", points[max_i].x, points[max_i].y)
