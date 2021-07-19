class Point:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

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

def Sq(p1, p2, p3):
    a = p1.dist_to(p2)
    b = p2.dist_to(p3)
    c = p3.dist_to(p1)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

points_red=[]
points_green=[]
for point in points:
    if point.color=="red":
        points_red.append(point)
    else:
        points_green.append(point)

print("Площадь красного треугольника = ", Sq(*points_red))
print("Площадь зеленого треугольника = ", Sq(*points_green))
