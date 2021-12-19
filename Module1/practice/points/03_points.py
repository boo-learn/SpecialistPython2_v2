class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
point_zero = Point(0, 0)
# TODO: your core here...

def distance(p1, p2):
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5

MIN = 0
MAX = 0
for i in range(0, len(points)):
    MIN = distance(point_zero, points[i])
    if MIN > MAX:
        MAX = MIN
        result = [points[i].x, points[i].y]

print("Расстояние = ", MAX)
print("Координаты наиболее удаленной точки = ", result)
