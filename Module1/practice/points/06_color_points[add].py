from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
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
red_point = []
red_sides = []
green_point = []
green_sides = []
#Делаем массив из точек разных цветов
for point in points:
    if point.color == 'red':
        red_point.append(point)
    else:
        green_point.append(point)
#Находим 3 длины у каждого треугольника
red_sides.append(red_point[0].dist_to(red_point[1]))
red_sides.append(red_point[1].dist_to(red_point[2]))
red_sides.append(red_point[2].dist_to(red_point[0]))

green_sides.append(green_point[0].dist_to(green_point[1]))
green_sides.append(green_point[1].dist_to(green_point[2]))
green_sides.append(green_point[2].dist_to(green_point[0]))

red_square = 0
green_square = 0
red_square_p = ((red_sides[0]+ red_sides[1] + red_sides[2]))/2
green_square_p = ((green_sides[0]+ green_sides[1] + green_sides[2]))/2
red_square = (red_square_p * (red_square_p - red_sides[0]) * (red_square_p - red_sides[1]) * (red_square_p - red_sides[2]))**0.5
green_square = (green_square_p * (green_square_p - green_sides[0]) * (green_square_p - green_sides[1]) * (green_square_p - green_sides[2]))**0.5


# your core here...

print("Площадь красного треугольника = ", red_square)
print("Площадь зеленого треугольника = ", green_square)
