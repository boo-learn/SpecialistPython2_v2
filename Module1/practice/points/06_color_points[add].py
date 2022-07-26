class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник
red_triangle = [point for point in points if point.color == "red"]
green_triangle = [point for point in points if point.color == "green"]


# Площадь треугольника по формуле Герона
def s_triangle(triangle):
    a = triangle[0].dist_to(triangle[1])
    b = triangle[1].dist_to(triangle[2])
    c = triangle[2].dist_to(triangle[0])
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


print("Площадь красного треугольника = ", s_triangle(red_triangle))
print("Площадь зеленого треугольника = ", s_triangle(green_triangle))
