class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        '''
        Расстояние от текущей точки до другой
        :param other_point: объект типа Point
        :return: возвращает скалярное расстояние между двумя точками
        '''
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def area_triangle(p1: Point, p2: Point, p3: Point):
    '''
    Площадь треугольника
    :param p1: объект типа Point
    :param p2: объект типа Point
    :param p3: объект типа Point
    :return: Площадь треугольника
    '''
    p = (p1.dist_to(p2) + p2.dist_to(p3) + p3.dist_to(p1)) / 2
    return (p * (p - p1.dist_to(p2)) * (p - p2.dist_to(p3)) * (p - p3.dist_to(p1))) ** 0.5


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

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов
pl1 = []
pl2 = []

# TODO: your core here...
for pnt in points:
    if pnt.color == "red":
        pl1.append(pnt)
    if pnt.color == "green":
        pl2.append(pnt)

print("Площадь красного треугольника = ", area_triangle(pl1[0], pl1[1], pl1[2]))
print("Площадь зеленого треугольника = ", area_triangle(pl2[0], pl2[1], pl2[2]))
