from math import sqrt

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def distance(p1, p2):
    return sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))



# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


max_distance = 0
max_ind = 0

for point in points:
    if max_distance < distance(point, Point()):
        max_distance = distance(point, Point())

for point in points:
    if distance(point, Point()) == max_distance:
        print(f"x:{point.x}, y:{point.y}")
