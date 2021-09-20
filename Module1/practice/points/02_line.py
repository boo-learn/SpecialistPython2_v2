class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1,p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** (1 / 2)

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
sum_dist = 0
for i in range(len(points)-1):
    dist = distance(points[i],points[i+1])
    sum_dist += dist


print("Длина ломаной линии = ", sum_dist)
