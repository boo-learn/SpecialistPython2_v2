from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
total_length = 0

for idx in range(len(points) - 1):
    total_length += points[idx].dist_to(points[idx + 1])
    print(idx)

print(f"Длина ломаной линии = {total_length:.2f}")

