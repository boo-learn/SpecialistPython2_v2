class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
points = [Point(0, 4), Point(0, 5), Point(0, 7)]
# TODO: Найдите длину ломаной линии

l = 0
dist=0
for i in range(len(points) - 1):
    dist = points[i].dist_to(points[i + 1])
    l += dist
    i += i

print("Длина ломаной линии = ", l)
