from math import sqrt


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        """Расстояние между двумя точками"""
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


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
# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов


class Triangle:
    """Треугольник создающийся из трех точек"""
    def __init__(self, a: Point, b: Point, c: Point):
        self.point_a = a
        self.point_b = b
        self.point_c = c
        self.side_a_b = self.dist_to(self.point_a, self.point_b)
        self.side_b_c = self.dist_to(self.point_b, self.point_c)
        self.side_a_c = self.dist_to(self.point_a, self.point_c)
        self.p = self.perimeter()
        self.s = self.square()

    @staticmethod
    def dist_to(point1, point2):
        """Расстояние между двумя точками"""
        return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    def perimeter(self):
        """Вычисляет периметр треугольника"""
        return self.side_a_b + self.side_b_c + self.side_a_c

    def square(self):
        """Вычисляет площадь треугольника по трём его сторонам и полупериметру"""
        pp = self.p / 2
        return sqrt(pp * (pp - self.side_a_b) * (pp - self.side_b_c) * (pp - self.side_a_c))


def generate_triangle(points_list: list, color: str):
    """Ищет три точки одного цвета и создаёт треугольник"""
    trg_points = []
    for point in points_list:
        if point.color == color:
            trg_points.append(point)
    return Triangle(a=trg_points[0], b=trg_points[1], c=trg_points[2])


if __name__ == '__main__':
    print(f"Площадь красного треугольника = {generate_triangle(points, 'red').s}")
    print(f"Площадь зеленого треугольника = {generate_triangle(points, 'green').s}")
