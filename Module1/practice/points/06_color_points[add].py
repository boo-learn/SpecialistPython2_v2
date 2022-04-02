class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

    def dist_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y) ** 2) ** 0.5

    def square(self, p1, p2):
        d1 = self.dist_to(p1)
        d2 = self.dist_to(p2)
        d3 = p1.dist_to(p2)
        p = 0.5 * (d1 + d2 + d3)
        return (p * (p - d1) * (p - d2) * (p - d3)) ** 0.5

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
    if point.color == "red":
        red_points.append(point)
    else:
        green_points.append(point)

print("Площадь красного треугольника = ", red_points[0].square(red_points[1], red_points[2]))
print("Площадь зеленого треугольника = ", green_points[0].square(green_points[1], green_points[2]))
