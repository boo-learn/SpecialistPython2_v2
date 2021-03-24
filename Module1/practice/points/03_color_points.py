import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def square_triangle(point_1, point_2, point_3):
    side_1 = point_1.dist_to(point_2)
    side_2 = point_2.dist_to(point_3)
    side_3 = point_3.dist_to(point_1)
    half_perimetr = (side_1 + side_2 + side_3) / 2
    return math.sqrt(half_perimetr
                     * (half_perimetr - side_1)
                     * (half_perimetr - side_2)
                     * (half_perimetr - side_3))


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

for i in range(len(points)):
    print(points[i].color)

red_points = []
green_points = []
for i in range(len(points)):
    if points[i].color == 'red':
        red_points.append(points[i])
    else:
        green_points.append(points[i])
print(red_points)
print(green_points)

red_square = square_triangle(*red_points)
green_square = square_triangle(*green_points)

print("Площадь красного треугольника = ", red_square)
print("Площадь зеленого треугольника = ", green_square)
