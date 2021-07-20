import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return math.sqrt((self.y - other_point.y) ** 2 + (self.x - other_point.x) ** 2)


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
def triangle_area(a1, a2, a3):
    p = (a1 + a2 + a3) / 2
    return math.sqrt(p * (p - a1) * (p - a2) * (p - a3))


def choose_color_triangle(color):
    return list(filter(lambda x: x.color == color, points))


# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

reds = choose_color_triangle('red')
greens = choose_color_triangle('green')
print("Площадь красного треугольника = ",
      triangle_area(reds[0].dist_to(reds[1]), reds[0].dist_to(reds[2]), reds[1].dist_to(reds[2])))
print("Площадь зеленого треугольника = ",
      triangle_area(greens[0].dist_to(greens[1]), greens[0].dist_to(greens[2]), greens[1].dist_to(greens[2])))
