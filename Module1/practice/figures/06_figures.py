import math
# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = ((self.center_coords[0] - other_circle.center_coords[0]) ** 2 +
             (self.center_coords[1] - other_circle.center_coords[1]) ** 2) ** 0.5
        if d > self.radius + other_circle.radius or d < abs(self.radius - other_circle.radius):
            return False
        else:
            return True

    def area(self):
        return math.pi * self.radius ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point_1 = p1
        self.point_2 = p2
        self.point_3 = p3

    def perimeter(self):
        a = self.point_1.dist_to(self.point_2)
        b = self.point_1.dist_to(self.point_3)
        c = self.point_2.dist_to(self.point_3)
        return a + b + c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point_1.dist_to(self.point_2)
        b = self.point_1.dist_to(self.point_3)
        c = self.point_2.dist_to(self.point_3)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


figures = [
    Triangle(Point(2, 4), Point(6, 8), Point(-2, 10)),
    Triangle(Point(12, 3), Point(7, 7), Point(0, -10)),
    Circle((4, 8), 3),
    Triangle(Point(-8, -4), Point(6, -6), Point(6, 10)),
    Circle((-6, -8), 6),
    Circle((2, 2), 1),
    Circle((-5, 4), 5),
]

max_area = max(figures, key=lambda fig: fig.area())
# Не совсем понял, что надо вывести в итоге, поэтому вывел площадь
print(max_area.area())
