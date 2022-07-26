# Используя классы треугольника и окружности из предыдущих задач
# создайте список с произвольным набором фигур
# Найдите и выведите фигуры с наибольшей площадьюimport math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = Point(p1[0], p1[1])
        self.point2 = Point(p2[0], p2[1])
        self.point3 = Point(p3[0], p3[1])

    def perimeter(self):
        # Находим длины сторон треугольника:
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point1.dist_to(self.point3)
        return a + b + c

    def area(self):
        # Находим длины сторон треугольника:
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point1.dist_to(self.point3)
        # Полу-периметр:
        half_p = (a + b + c) / 2
        # Для нахождения площади, используйте формулу Герона
        return (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def length(self):
        """
        :return: длину окружности
        """
        return self.radius * 2 * math.pi

    def area(self):
        """
        :return: площадь окружности
        """
        return self.radius ** 2 * math.pi


figures_list = [
    Circle((0, 0), 5),
    Triangle((0, 0), (5, 3), (-2, 2)),
    Circle((-2, -4), 15)
]
# figure_num = 0
max_area = figures_list[0].area()
for figure in figures_list:
    if figure.area() > max_area:
        max_area = figure.area()
    figure_max = type(figure)
print(f"Самая большая фигура - {figure_max}, площадь - {max_area}")


