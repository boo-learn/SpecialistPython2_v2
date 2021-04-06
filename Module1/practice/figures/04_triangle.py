from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x  # создание координаты х точки
        self.y = y  # создание координаты у точки

    def dist_to(self, other_point): # расстояние между 2 точками
        return sqrt( ((other_point.x - self.x) ** 2) + ((other_point.y - self.y) ** 2) )


class Triangle:  # работа с треугольником
    def __init__(self, p1, p2, p3):
        self.point1 = p1  # создание точки А
        self.point2 = p2  # создание точки В
        self.point3 = p3  # создание точки С

    def perimeter(self):
        # поиск периметра треугольника
        self.dot_A = Point.dist_to(self.point1, self.point2)  # нахождение стороны АВ
        self.dot_B = Point.dist_to(self.point2, self.point3)  # нахождение стороны ВС
        self.dot_C = Point.dist_to(self.point1, self.point3)  # нахождение стороны СА
        self.per = self.dot_A + self.dot_B + self.dot_C  # нахождение периметра треугольника
        return self.per


    def area(self):  # поиск площади треугольника
        # Для нахождения площади, используйте формулу Герона
        self.per_05 = self.per / 2  # нахождение полупериметра треугольника
        self.pl = sqrt( self.per_05 * (self.per_05 - self.dot_A) * (self.per_05 - self.dot_B) * (self.per_05 - self.dot_C) )  # нахождение площади треугольника
        return self.pl


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 0))  # Создаем 3 точки в классе Triangle через конструктор класса Point
# Задание: найдите площадь и пеиметр треугольника, реализовав методы
perimetr_float = float(triangle1.perimeter())  # преобразование периметра в тип float
area_float = float(triangle1.area())  # преобразование площади в тип float

def toFixed(numObj, digits=0):  # функция форматирования числа типа float
    return f"{numObj:.{digits}f}"
# TODO: your core here...

print("Периметр треугольника = ", toFixed(perimetr_float, 1))  # вывод периметра треугольника в формате 1.0
print("Площадь треугольника = ", toFixed(area_float, 1))  # вывод площади треугольника в формате 1.0
