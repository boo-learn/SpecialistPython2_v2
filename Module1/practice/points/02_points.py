class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
def distance(p1: Point, p2: Point) -> float:
    dist = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
    return dist


# Дан список из произвольного количества точек:

points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]

# И произвольная точка на плоскости:
random_point = Point(-12, 10)
for point in points:

    point1 = random_point
    point2 = point
    dist = distance(point1, point2)
    print(dist)


# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py
