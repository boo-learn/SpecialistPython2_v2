from math import sqrt


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


def calc_trianle(tri_points):
    """
    S = v(p(p - a)(p - b)(p - c)),
    где
    a, b, c – стороны
    треугольника, p – полупериметр.p = (a + b + c) / 2
    """

    a = tri_points[0].dist_to(tri_points[1])
    b = tri_points[1].dist_to(tri_points[2])
    c = tri_points[2].dist_to(tri_points[0])
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


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


red_list = []
green_list = []

for point in points:
    if point.color == "red":
        red_list.append(point)
    if point.color == "green":
        green_list.append(point)

if len(red_list):
    print("Площадь красного треугольника = ", calc_trianle(red_list))

if len(green_list):
    print("Площадь зеленого треугольника = ", calc_trianle(green_list))
