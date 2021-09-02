import math
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p3 = p3
        self.p2 = p2
        self.p1 = p1

    def area(self):
        a = self.p1.dist_to(self.p2)
        b = self.p1.dist_to(self.p3)
        c = self.p2.dist_to(self.p3)
        hp = (a + b + c) / 2
        return math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))

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

red_points=list(filter(lambda x: x.color == "red", points))
print("Площадь красного треугольника = ", Triangle(red_points[0], red_points[1], red_points[2]).area())
green_points=list(filter(lambda x: x.color == "green", points))
print("Площадь зеленого треугольника = ", Triangle(green_points[0], green_points[1], green_points[2]).area())
