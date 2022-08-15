class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    res = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
    return res

# Дан список из произвольного количества точек:
points = [Point(2, 4), Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
# random_point = Point(-12, 10)
random_point = Point(5, -2)

# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py

for i in points:
    res = distance(i, random_point)
    print(res)

