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


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())
