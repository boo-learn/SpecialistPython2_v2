# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

import math

class Point:
    def __init__(self, coords):
        self.x = float(coords[0])
        self.y = float(coords[1])

    def dist_to(self, op):
        return ((self.x - op.x) ** 2 + (self.y - op.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        perim = (
            self.point1.dist_to(self.point2)
            + self.point2.dist_to(self.point3)
            + self.point3.dist_to(self.point1)
        )
        return perim

    def area(self):
        p_half = self.perimeter() / 2
        s = (
            p_half
            * (p_half - self.point1.dist_to(self.point2))
            * (p_half - self.point2.dist_to(self.point3))
            * (p_half - self.point3.dist_to(self.point1))
        ) ** 0.5
        return s


class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords.x
        self.y = center_coords.y
        self.rad = float(radius)

    def area(self):
        s = math.pi * self.rad ** 2
        return s


fig_num = int(input("Введите количество фигур в списке: "))
fig_list = []
point1 = Point
point2 = Point
point3 = Point
rad = 0
coords = []
max_area = 0
for i in range(fig_num):
    typef = 0
    while typef not in (1, 2):
        typef = int(input("Выберите тип фигуры.\n1 - Треугольник, 2 - Окружность:\n"))
    if typef == 1:
        print("Введите координаты точек:")
        coords = input("Для точки 1:\n")
        point1 = Point(coords.split(sep=", "))
        coords = input("Для точки 2:\n")
        point2 = Point(coords.split(sep=", "))
        coords = input("Для точки 3:\n")
        point3 = Point(coords.split(sep=", "))
        a = Triangle(point1, point2, point3)
        fig_list.append(a)
        if max_area < a.area():
            max_area = a.area()
    if typef == 2:
        coords = input("Введите координаты центра:\n")
        point1 = Point(coords.split(sep=", "))
        rad = input("Введите радиус окружности:\n")
        a = Circle(point1, rad)
        fig_list.append(a)
        if max_area < a.area():
            max_area = a.area()
print("Фигуры с максимальной площадью:")
j = 0
for a in fig_list:
    j += 1
    if a.area() == max_area:
        print(f"{j}:", end=" ")
        if type(a) == Circle:
            print(
                f"Circle\n x: {a.x}, y: {a.y}\n Радиус: {a.rad}\n Площадь: {a.area()}"
            )
        if type(a) == Triangle:
            print(
                f"Triangle\n x1: {a.point1.x}, y1: {a.point1.y}\n x2: {a.point2.x}, y2: {a.point2.y}\n x3: {a.point3.x}, y3: {a.point3.y}\n Площадь: {a.area()}"
            )

