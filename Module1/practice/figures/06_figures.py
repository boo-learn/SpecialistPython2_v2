# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью

from random import randint as rnd

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + \
                (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def __repr__(self):
        return f'Треугольник с вершинами {self.point1}, {self.point2}, {self.point3}'

    def perimeter(self):
        per = self.point1.dist_to(self.point2)
        per += self.point2.dist_to(self.point3)
        per += self.point3.dist_to(self.point1)
        return per
        

    def area(self):
        lines = [self.point1.dist_to(self.point2),
                 self.point2.dist_to(self.point3),
                 self.point3.dist_to(self.point1)]
        half_per = self.perimeter() / 2        
        area = (half_per * (half_per - lines[0]) * (half_per - lines[1]) * \
        (half_per - lines[2])) ** 0.5        
        return area


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f'Круг с центром в {self.center} и радиусом {self.radius}'

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = ((self.center.x - other_circle.center.x) ** 2 + \
                (self.center.y - other_circle.center.y) ** 2) ** 0.5        
        return dist <= self.radius + other_circle.radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

list_of_figures = []

for _ in range(rnd(1, 3)):
    points = []
    for i in range(3):
        x = rnd(-20, 20)
        y = rnd(-20, 20)
        points.append(Point(x, y))
    list_of_figures.append(Triangle(*points))

for _ in range(rnd(1, 3)):
    x = rnd(-20, 20)
    y = rnd(-20, 20)
    r = rnd(1, 10)
    list_of_figures.append(Circle(Point(x, y), r))

areas = [round(figure.area(), 2) for figure in list_of_figures]


max_area = max(areas)
for figure in list_of_figures:
    if round(figure.area(), 2) == max_area :
        print(f'{figure}, площадью {max_area} имеет максимальную площадь.')            
