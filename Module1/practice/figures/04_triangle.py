class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5



class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        return self.point1.dist_to(self.point2) + self.point2.dist_to(self.point3) + self.point3.dist_to(self.point1)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        p = (a + b + c) / 2
        return (p(p - a)(p - b)(p - c)) ** 0.5
        

# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())
