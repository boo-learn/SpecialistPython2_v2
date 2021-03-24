class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def square(self, point_1, point_2):
        sides =[0, 0, 0]
        sides[0] = self.dist(point_1)
        sides[1] = self.dist(point_2)
        sides[2] = point_1.dist(point_2)
        half_p = sum(sides) / 2
        return (half_p * (half_p - sides[0]) * (half_p - sides[1]) * (half_p - sides[2])) ** 0.5



# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(5, 5, "red"),
    Point(0, 4, "green"),
    Point(5, 0, "red"),
    Point(0, 0, "green"),
    Point(4, 0, "green"),
    Point(0, 5, "red")
]
# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

points_green, points_red = [],[]
for p in points:
    if p.color == "green":
        points_green.append(p)
    else:
        points_red.append(p)


print("Площадь красного треугольника = ", points_red[0].square(points_red[1], points_red[2]))
print("Площадь зеленого треугольника = ", points_green[0].square(points_green[1], points_green[2]))
