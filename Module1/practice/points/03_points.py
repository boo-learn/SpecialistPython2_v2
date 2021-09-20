class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1,p2):
    # TODO: your code here
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

start_point = Point(0,0)

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...

dist = float()
max_point = Point(0, 0)

for point in points:
    dist1 = distance(start_point, point)
    if dist1 > dist:
        dist = dist1
        max_point = point




print("Координаты наиболее удаленной точки = ", f"({max_point.x};{max_point.y})")
