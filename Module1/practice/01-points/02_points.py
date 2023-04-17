class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x1 - x2) * 2 + (y1 - y2) * 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
for point in points:
    d = distance(random_point.x, random_point.y, point.x, point.y)
    print(f"Расстояние между точкой ({point.x}, {point.y}) и точкой ({random_point.x}, {random_point.y}) равно {d}")
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py
