# Используя классы треугольника и окружности из предыдущих задач
# создайте список с набором фигур
# Найдите и выведите фигуры с наибольшей площадью
import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimetr(self):
        side_1 = self.point1.dist_to(self.point2)
        side_2 = self.point2.dist_to(self.point3)
        side_3 = self.point3.dist_to(self.point1)
        return side_1 + side_2 + side_3

    def area(self):
        p = self.perimetr()
        side_1 = self.point1.dist_to(self.point2)
        side_2 = self.point2.dist_to(self.point3)
        side_3 = self.point3.dist_to(self.point1)
        half_perimetr = p / 2
        return math.sqrt(half_perimetr
                         * (half_perimetr - side_1)
                         * (half_perimetr - side_2)
                         * (half_perimetr - side_3))


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = Point(*center_coords)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


figures_type = ['Triangle', 'Circle']
count = int(input('ВВедите количество фигур в списке: '))
lst = []
random_coords = []

for i in range(count):
    lst.append(random.choice(figures_type))
print(lst)

for i in range(len(lst)):
    if lst[i] == 'Triangle':
        random_point_1 = Point(random.randint(-100, 100), random.randint(-100, 100))
        random_point_2 = Point(random.randint(-100, 100), random.randint(-100, 100))
        random_point_3 = Point(random.randint(-100, 100), random.randint(-100, 100))
        lst[i] = Triangle(random_point_1, random_point_2, random_point_3)

    else:
        random_coords.append(random.randint(-100, 100))
        random_coords.append(random.randint(-100, 100))
        random_radius = random.randint(0, 100)
        lst[i] = Circle(random_coords, random_radius)
        random_coords = []

print(lst)

max_area = 0
result = ''
for figure in lst:
    current_area = figure.area()
    # print(f'Фигура № {lst.index(figure)+1}')
    # print(f'Тип: {"Круг" if type(figure) == "__main__.Circle" else "Треугольник"}')
    # print(f'Площадь: {current_area} кв. ед.')
    if current_area > max_area:
        max_area = current_area
        result = figure

print(f'Максимальная площадь {int(round(max_area, 0))} кв. ед. у фигуры № {lst.index(result) + 1} '
      f'типа {"Круг" if type(result) == "__main__.Circle" else "Треугольник"}')
