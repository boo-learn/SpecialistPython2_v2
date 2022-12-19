from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point0 = Point(0,0)

maxd = 0
maxn = 0

for p in points:
    dist = round(p.dist_to(point0), 3)
    if dist > maxd:
        maxd = dist
        maxn += 1
    print(f"x = {p.x}, y = {p.y}, d = {round(p.dist_to(point0), 3)}")
    
print(f"Координаты наиболее удаленной точки = ({points[maxn].x}, {points[maxn].y}, Дистанция: {maxd}")

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты

print("Координаты наиболее удаленной точки = ", ...)
