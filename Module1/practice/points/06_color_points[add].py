from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def triangle_area(triangle_points):
    a = triangle_points[0].dist_to(triangle_points[1])
    b = triangle_points[0].dist_to(triangle_points[2])
    c = triangle_points[1].dist_to(triangle_points[2])
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to()
# TODO-3: вычислите площади треугольников образованных точками разных цветов

# your core here...
red_triangle = []
green_triangle = []

for point in points:
    if point.color == 'red':
        red_triangle.append(point)
    elif point.color == 'green':
        green_triangle.append(point)

print("Площадь красного треугольника = ", triangle_area(red_triangle))
print("Площадь зеленого треугольника = ", triangle_area(green_triangle))
