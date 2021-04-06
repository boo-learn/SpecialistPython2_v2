# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5



class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.a = self.point1.dist_to(self.point2)
        self.b = self.point2.dist_to(self.point3)
        self.c = self.point3.dist_to(self.point1)

    def perimeter(self):
        # Периметр треугольника
        return self.a + self.b + self.c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        return (self.perimeter() / 2 * (self.perimeter() / 2 - self.a) * \
                                       (self.perimeter() / 2 - self.b) * \
                                       (self.perimeter() / 2 - self.c)) ** 0.5


class Circle:
    def __init__(self, center_coords: Point, radius):
        self.center = center_coords
        self.radius = radius

    def area(self):
        # Для нахождения площади
        return math.pi * (self.radius ** 2)

figures = [Circle(Point(3, 4), 5), Triangle(Point(3, -4), Point(3, 5), Point(4, 4)), \
           Triangle(Point(5, 8), Point(1, 3), Point(-5, 3)), Circle(Point(7, -5), 3), \
           Circle(Point(2, 1), 6), Triangle(Point(-5, -9), Point(9, 13), Point(5, 7))]

figures.sort(reverse=True, key=lambda fig:fig.area())

print('Площади фигур в порядке убывания')
for fig in figures:
    print(f"{f'(({fig.center.x}, {fig.center.y}), {fig.radius})' if 'Circle' in str(type(fig)) else f'(({fig.point1.x}, {fig.point1.y}),... )'} = {fig.area():.2f}")
