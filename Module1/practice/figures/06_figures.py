# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью


from math import sqrt, pi
import random


class Point:
    """Точка в двоичной системе координат"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}:{self.y})'

    def __repr__(self):
        return self.__str__()

    def dist_to(self, other_point):
        """Расстояние между двумя точками"""
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


class Circle:
    """Окружность по координатам центра и радиусу"""
    def __init__(self, center_coords: Point, radius: float):
        self.center_coords = center_coords
        self.radius = radius
        self.s = self.area()
        self.p = self.perimeter()

    def __str__(self):
        return f'Circle in coords {self.center_coords}, r = {round(self.radius, 2)}, ' \
               f'p = {round(self.s, 2)}, s = {round(self.s, 2)}'

    def __repr__(self):
        return f'Circle: coords={self.center_coords}, r={self.radius}'

    def intersect(self, other_circle) -> bool:
        """Проверяет пересекается ли текущая окружность с окружностью other_circle"""
        radii = [self.radius, other_circle.radius]  # оказывается радиус в множественном числе - это radii
        dist = self.center_coords.dist_to(other_circle.center_coords)
        if dist > sum(radii) or dist < min(radii):
            return False
        else:
            return True

    def area(self):
        """Вычисляет площадь окружности"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Вычисляет площадь окружности"""
        return 2 * pi * self.radius


class Triangle:
    """Треугольник который генерируется из трёх точек"""
    def __init__(self, a: Point, b: Point, c: Point):
        self.point_a = a
        self.point_b = b
        self.point_c = c
        self.side_a_b = self.dist_to(self.point_a, self.point_b)
        self.side_b_c = self.dist_to(self.point_b, self.point_c)
        self.side_a_c = self.dist_to(self.point_a, self.point_c)
        self.p = self.perimeter()
        self.s = self.area()

    def __str__(self):
        return f'Triangle in coords a={self.point_a}, b={self.point_b}, c={self.point_c} ' \
               f'p = {round(self.p, 2)}, s = {round(self.s, 2)}'

    def __repr__(self):
        return f'Triangle a={self.point_a}, b={self.point_b}, c={self.point_c}'

    @staticmethod
    def dist_to(point1, point2):
        """Расстояние между двумя точками"""
        return sqrt(((point1.x - point2.x) ** 2) + ((point1.y - point2.y) ** 2))

    def perimeter(self):
        """Вычисляет периметр треугольника"""
        return self.side_a_b + self.side_b_c + self.side_a_c

    def area(self):
        """Вычисляет площадь треугольника по трём его сторонам и полупериметру"""
        pp = self.p / 2     # Честно говоря, не помню что такое формула Герона, надеюсь это она)))
        return sqrt(pp * (pp - self.side_a_b) * (pp - self.side_b_c) * (pp - self.side_a_c))


def get_rand_coord() -> int:
    """Генерирует рандомную координату (одно целове число)"""
    return random.randint(-50, 50)


def generate_figures_list() -> list:
    """Генерирует список объектов фигур"""
    figures_types = ['circle', 'triangle']
    res = []
    for i in range(random.randint(5, 15)):
        figure_type = figures_types[random.randint(0, 1)]
        if figure_type == 'triangle':
            res.append(
                Triangle(
                    a=Point(get_rand_coord(), get_rand_coord()),
                    b=Point(get_rand_coord(), get_rand_coord()),
                    c=Point(get_rand_coord(), get_rand_coord()),
                )
            )
        elif figure_type == 'circle':
            res.append(
                Circle(
                    center_coords=Point(get_rand_coord(), get_rand_coord()),
                    radius=random.randint(1, 20)
                )
            )
        else:
            raise IndexError
    return res


def get_biggest_figures(figures_list: list) -> list:
    """Получает список фигур и возвращает самые крупные каждого вида"""
    biggest_triangle = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))
    biggest_circle = Circle(Point(0, 0), 0)
    for figure in figures_list:
        if figure.__class__ == Circle:
            if figure.s > biggest_circle.s:
                biggest_circle = figure
        elif figure.__class__ == Triangle:
            if figure.s > biggest_triangle.s:
                biggest_triangle = figure
        else:
            raise IndexError
    return [biggest_circle, biggest_triangle]


if __name__ == '__main__':
    generated_figures_list = generate_figures_list()
    print(f'In figures: {generated_figures_list}')
    biggest_figures = get_biggest_figures(generated_figures_list)
    for figure in biggest_figures:
        print(f'Biggest {figure}')
