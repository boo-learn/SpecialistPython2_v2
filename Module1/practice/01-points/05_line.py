from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
total_length = 0
for i in range(len(points) - 1):
    segment_length = points[i].dist_to(points[i+1])
    total_length += segment_length

rounded_length = round(total_length)
print("Длина ломаной линии = ", rounded_length)
