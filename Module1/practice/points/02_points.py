class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**.5


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

# TODO: выведите расстояние от каждой точки(из списка) до точки random_point
# Совет: используйте функцию distance() из предыдущего задания
# Подсказка: смотри пример, Module1/examples/05_objects_list.py

# Переберем все точки циклом и выведем их координаты в нужном нам формате(виде)
for point in points:
    print(distance(point, random_point))
