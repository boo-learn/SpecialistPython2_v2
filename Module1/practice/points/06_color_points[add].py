import math


class Point:
    def __init__(self, x, y, c='white'):
        self.x = x
        self.y = y
        self.color = c

    def dist_to(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

    def triangle_s(self, B, C):
        a = self.dist_to(B)
        b = self.dist_to(C)
        c = B.dist_to(C)
        p = (a + b + c) * 0.5

        return math.sqrt(p * (p - a) * (p - b) * (p - c))


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
red_points = []
green_points = []
color1 = 'red'
color2 = 'green'
for point in points:
    if point.color == color1:
        red_points.append(point)
    elif point.color == color2:
        green_points.append(point)

print("Площадь красного треугольника = ", red_points[0].triangle_s(red_points[1],red_points[2]))
print("Площадь зеленого треугольника = ", green_points[0].triangle_s(green_points[1],green_points[2]))
