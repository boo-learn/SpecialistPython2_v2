class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        round(((self.x - other_point.x) ** 2 +
               (self.y - other_point.y) ** 2) ** 0.5, 2)


def square(points):
    x1, y1, x2, y2, x3, y3 = [points[0].x, points[0].y,
                              points[1].x, points[1].y,
                              points[2].x, points[2].y]
    return abs(0.5 * ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)))


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

red = [i for i in points if i.color == 'red']
green = [i for i in points if i.color == 'green']

print("Площадь красного треугольника = ", square(red))
print("Площадь зеленого треугольника = ", square(green))
