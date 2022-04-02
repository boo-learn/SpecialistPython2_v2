import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


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
# Все точки одного цвета соединены линиями и образуют треугольник

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to()
# TODO-3: вычислите площади треугольников образованных точками разных цветов

def square_of_triangle(a,b,c):
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

# your core here...
points_red, points_green=[]
for point in points:
    if point.color=="red":
        points_red.append(point)
    else:
        points_green.append(point)
red_square=square_of_triangle(points_red[0].dist_to(points_red[1]),points_red[1].dist_to(points_red[2]),points_red[0].dist_to(points_red[2]))
green_square=square_of_triangle(points_green[0].dist_to(points_green[1]),points_green[1].dist_to(points_green[2]),points_green[0].dist_to(points_green[2]))
print("Площадь красного треугольника = ", red_square)
print("Площадь зеленого треугольника = ", green_square)
