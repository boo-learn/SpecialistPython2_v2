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
red_points = []
green_points = []

for point in points:
    if point.color == 'red':
        red_points.append(point)
    else:
        green_points.append(point)


def triangle_square(points):
    return 0.5 * abs((points[1].x - points[0].x) * (points[2].y - points[0].y) - (points[2].x - points[0].x) * (
                points[1].y - points[0].y))


print("Площадь красного треугольника = ", triangle_square(red_points))
print("Площадь зеленого треугольника = ", triangle_square(green_points))
