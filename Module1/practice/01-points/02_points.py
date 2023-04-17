class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py
def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    return (((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)) ** 0.5


for point in points:
    print(distance(point, random_point))
