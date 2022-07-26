class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        if other_point.color == self.color:
            return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5
        else:
            return 0


def triangle_area(p1, p2, p3):
    distp1_p2 = p1.dist_to(p2)
    distp2_p3 = p2.dist_to(p3)
    distp3_p1 = p3.dist_to(p1)
    semiperimeter = (distp1_p2 + distp2_p3 + distp3_p1) * 0.5
    area = (semiperimeter * (semiperimeter - distp1_p2) * (semiperimeter - distp2_p3) * (
            semiperimeter - distp3_p1)) ** 0.5
    return area


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
    if point.color == "green":
        green_triangle.append(point)
    else:
        red_triangle.append(point)

# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный

# Все точки одного цвета соединены линиями и образуют треугольник

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to()
# TODO-3: вычислите площади треугольников образованных точками разных цветов

# your core here...

print("Площадь красного треугольника = ", triangle_area(red_triangle[0], red_triangle[1], red_triangle[2]))
print("Площадь зеленого треугольника = ", triangle_area(green_triangle[0], green_triangle[1], green_triangle[2]))

