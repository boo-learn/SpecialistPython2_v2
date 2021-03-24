class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

 
def triangle_area(point_1, point_2, point_3):
        a = point_1.dist_to(point_2)
        b = point_1.dist_to(point_3)
        c = point_2.dist_to(point_3)
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
points_green = []
points_red = []

# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов

# TODO: your core here...
points_green = list(filter(lambda point: point.color == "green", points))
points_red = list(filter(lambda point: point.color == "red", points))

print("Площадь красного треугольника = ", triangle_area(points_red[0], points_red[1], points_red[2]))
print("Площадь зеленого треугольника = ", triangle_area(points_green[0], points_green[1], points_green[2]))
