from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        return (((self.x - other_point.x)**2) + ((self.y - other_point.y)**2))**0.5

    def max_length_to_point(self, points: list):
        distance_to_zero = []
        for point in points:
            distance_to_zero.append(self.dist_to(point))

        max_point = distance_to_zero[0]
        for point in distance_to_zero:
            if point > max_point:
                max_point = point
        return max_point

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def max_length_to_point(point: Point):
    distance_to_zero = []
    for point in points:
        distance_to_zero.append(zero.dist_to(point))

    max_point = distance_to_zero[0]
    for point in distance_to_zero:
        if point > max_point:
            max_point = point
    return max_point
    
zero = Point(0, 0)

print("Координаты наиболее удаленной точки = ", zero.max_length_to_point(points))
print("Координаты наиболее удаленной точки = ", max_length_to_point(zero))
