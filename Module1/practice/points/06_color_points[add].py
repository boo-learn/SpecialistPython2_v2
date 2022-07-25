import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


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

# your core here...

red_points = []
green_points = []

for p in points:
    if p.color == "red":
        red_points.append(p)
    if p.color == "green":
        green_points.append(p)

red_s = 0.5 * ((red_points[1].x - red_points[0].x) * (red_points[2].y - red_points[0].y) - (red_points[2].x - red_points[0].x) * (red_points[2].y - red_points[1].y))
green_s = 0.5 * ((green_points[1].x - green_points[0].x) * (green_points[2].y - green_points[0].y) - (green_points[2].x - green_points[0].x) * (green_points[2].y - green_points[1].y))


print("Площадь красного треугольника = ", red_s)
print("Площадь зеленого треугольника = ", green_s)
