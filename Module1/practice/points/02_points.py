import math

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, 8), Point(10, 8), Point(0, 8), Point(-12, 8)]
# И произвольная точка на плоскости:
random_point = Point(-12, 8)

for p in points:
    print(distance(p, random_point))
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py
