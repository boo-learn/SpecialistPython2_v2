class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point) -> float:
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    p1x = p1.x
    p1y = p1.y
    p2x = p2.x
    p2y = p2.y
    result = (((p1x - p2x)**2) + ((p1y - p2y)**2))**0.5
    return float(result)

# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

distance_to_point = []
for point in points:
    distance_to_point.append(distance(random_point, point))

print(distance_to_point)

# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py
