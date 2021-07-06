# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = self.p1.dist_to(self.p2)
        b = self.p1.dist_to(self.p3)
        c = self.p2.dist_to(self.p3)
        hp = (a + b + c) / 2
        return (hp * (hp - a) * (hp - b) * (hp - c)) ** 0.5

    def __str__(self):
        return "треугольник"


class Circle:
    def __init__(self, cc, rad):
        self.cc = Point(*cc)
        self.rad = rad

    def area(self):
        return 3.14 * self.rad ** 2

    def __str__(self):
        return "круг"


figures = [Circle((6, -8), 5), (Triangle(Point(2, 4), Point(10, 8), Point(-2, -8))), Circle((4, -5), 6),
           (Triangle(Point(2, 1), Point(155, 158), Point(-152, -154)))]

max_fig_area = 0
max_fig = None
for fig in figures:
    if fig.area() > max_fig_area:
        max_fig_area = fig.area()
        max_fig = fig

print(f'Наибольшей фигурой является {max_fig} с площадью {max_fig_area}')
