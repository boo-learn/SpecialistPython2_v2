class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5


summa = 0
d = distance(points[0],points[1])
summa += d
d = distance(points[1],points[2])
summa += d
d = distance(points[2],points[3])
summa += d
d = distance(points[3],points[4])



print("Длина ломаной линии = ", summa)
