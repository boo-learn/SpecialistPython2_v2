class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def square_triangle(point_a, point_b, point_c):
    a = point_a.dist_to(point_b)
    b = point_b.dist_to(point_c)
    c = point_c.dist_to(point_a)
    half_p = (a + b + c)/2
    return (half_p * (half_p - a) * (half_p - b) * (half_p - c)) * 0.5


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
red_points = []
green_points = []
for p in points:
    if p.color == "red":
        red_points.append(p)
    elif p.color == "green":
        green_points.append(p)

# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

# TODO: your core here...

print("Площадь красного треугольника = ", square_triangle(*red_points))
print("Площадь зеленого треугольника = ", square_triangle(*green_points))
