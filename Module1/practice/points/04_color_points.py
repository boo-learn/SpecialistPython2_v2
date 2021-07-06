class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def triangle_area(p1, p2, p3):
    a = p1.dist_to(p2)
    b = p2.dist_to(p3)
    c = p1.dist_to(p3)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


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

red_triangle = []
green_triangle = []
for point in points:
    if point.color == 'red':
        red_triangle.append(point)
    else:
        green_triangle.append(point)

# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

print("Площадь красного треугольника = ", triangle_area(*red_triangle))
print("Площадь зеленого треугольника = ", triangle_area(*green_triangle))
