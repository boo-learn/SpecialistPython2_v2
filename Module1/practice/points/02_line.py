import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)
# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
l=0
for i in range (0,len(points)-1):
    l+=distance(points[i], points[i+1])


print("Длина ломаной линии = ", format(l, '.2f'))
