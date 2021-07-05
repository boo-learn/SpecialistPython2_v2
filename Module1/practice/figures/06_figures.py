import math
# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        '''
        Расстояние от текущей точки до другой
        :param other_point: объект типа Point
        :return: возвращает скалярное расстояние между двумя точками
        '''
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def show(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        '''
        Периметр треугольника
        :return: Возвращает периметр треугольника
        '''
        return (self.point1.dist_to(self.point2) + self.point2.dist_to(self.point3) + self.point3.dist_to(self.point1))

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        '''
        Площадь треугольника, посчитанная по формуле Герона
        :return: Площадь треугольника
        '''
        p = self.perimeter()/2
        return (p * (p - self.point1.dist_to(self.point2)) * (p - self.point2.dist_to(self.point3)) * (p - self.point3.dist_to(self.point1))) ** 0.5

    def show(self):
        return 'Треугольник с координатами (' + str(self.point1.show()) + '' + str(self.point2.show()) + '' + str(self.point3.show())


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = ((self.center_coords.x - other_circle.center_coords.x) ** 2 + (self.center_coords.y - other_circle.center_coords.y) ** 2) ** 0.5
        if d > abs(self.radius - other_circle.radius):
            return False
        else:
            return True

    def area(self):
        return math.pi * (self.radius ** 2)

    def show(self):
        return 'Круг с центром координат ' + str(self.center_coords.show())


figures = [Triangle(Point(2, 4), Point(12, 8), Point(-2, 0)), Circle(Point(0, 0), 15), Circle(Point(2, 0), 5)]

max_area = 0

for fig in figures:
    if fig.area() > max_area:
        max_area = fig.area()
        max_fig = fig

print (f'{max_fig.show()} и площадью {max_area}')
