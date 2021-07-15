
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

o = Point(0,0)
l_max=distance(o, points[0])
for el in points:
    if distance(o, el)>l_max:
        l_max= distance(o, el)
        c_max = el


print("Координаты наиболее удаленной точки = ", c_max.x, c_max.y)
