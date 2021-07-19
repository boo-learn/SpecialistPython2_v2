import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)
# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
line_sum = sum([distance(points[i], points[i+1]) for i, _ in enumerate(points) if i + 1 != len(points)])
print("Длина ломаной линии = ", line_sum)
