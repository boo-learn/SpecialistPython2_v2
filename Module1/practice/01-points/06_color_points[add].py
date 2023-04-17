from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def area(self) -> float:
        ab = self.point1.dist_to(self.point2)
        ac = self.point1.dist_to(self.point3)
        bc = self.point2.dist_to(self.point3)
        half_p = (ab + ac + bc) / 2

        return (half_p * (half_p - ab) * (half_p - ac) * (half_p - bc)) ** 0.5


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три, но порядок точек в списке и значение координат произвольные
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
# TODO-2: реализуйте метод dist_to(), для расчета расстояния между точками
# TODO-3: вычислите площади треугольников образованных точками разных цветов

red_tringle_points = []
green_tringle_points = []

for p in points:
    if p.color == "red":
        red_tringle_points.append(p)
    else:
        green_tringle_points.append(p)

red_tringle = Triangle(*red_tringle_points)
green_tringle = Triangle(*green_tringle_points)

print(f"Площадь красного треугольника = {red_tringle.area()}")
print(f"Площадь зеленого треугольника = {green_tringle.area()}")
