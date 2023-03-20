from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        return (((self.x - other_point.x)**2) + ((self.y - other_point.y)**2))**0.5
    
    def length_line(self, points_list: list[Point]):
        length = []
        for element in range(len(points_list)):
            if element+1 != len(points_list):
                p2 = points_list[element+1]
                p1 = points_list[element]
                length.append(p1.dist_to(p2))
        return sum(length)


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии

length = []
for element in range(len(points)):
    if element+1 != len(points):
        p2 = points[element+1]
        p1 = points[element]
        length.append(p1.dist_to(p2))

from_func = sum(length)

from_class = Point(0, 0)

print("Длина ломаной линии = ", from_func)
print("Длина ломаной линии = ", from_class.length_line(points))
