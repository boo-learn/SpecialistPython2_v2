class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        return self.point1.dist_to(self.point2)+self.point2.dist_to(self.point3)+self.point1.dist_to(self.point3)

    def area(self):
       return (0.5*self.perimeter()*(0.5*self.perimeter()-self.point1.dist_to(self.point2))*(0.5*self.perimeter()-self.point2.dist_to(self.point3))*(0.5*self.perimeter()-self.point1.dist_to(self.point3)))


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...
p=triangle1.perimeter()
s=triangle1.area()
print("Периметр треугольника = %.2f" % p)
print("Площадь треугольника = %.2f" % s)
