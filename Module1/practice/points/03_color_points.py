#!/usr/bin
import math
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def triangle_square(self, second_point, third_point):
        return 0.5 * abs((self.x - third_point.x) * (second_point.y - third_point.y) - (second_point.x - third_point.x) * (self.y-third_point.y))

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

# TODO: your core here...
red_list = []
green_list = []
for point in points:
    if point.color == "red":
        red_list.append(point)
    elif point.color == "green":
        green_list.append(point)

red_square = red_list[0].triangle_square(red_list[1], red_list[2])
green_square = green_list[0].triangle_square(green_list[1], green_list[2])
print("Площадь красного треугольника = ", red_square)
print("Площадь зеленого треугольника = ", green_square)
