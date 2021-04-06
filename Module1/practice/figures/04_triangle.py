from math import sqrt


class Point:
    """Точка в двоичной системе координат"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        """Расстояние между двумя точками"""
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


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


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы


if __name__ == '__main__':
    print(f"Периметр треугольника = {round(triangle1.p, 2)}")
    print(f"Площадь треугольника = {round(triangle1.s, 2)}")
