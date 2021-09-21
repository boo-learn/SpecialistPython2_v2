import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return((point.x - self.x)**2 + (point.y - self.y))**.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.a = self.point1.dist_to(self.point2)
        self.b = self.point2.dist_to(self.point3)
        self.c = self.point3.dist_to(self.point1)

    def perimeter(self):
        return round(self.a+self.b+self.c)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        pl = self.perimeter()/2
        return round(math.sqrt(pl*((pl - self.a)*(pl - self.b) * (pl - self.c)))


# Треугольник задан координатами трех точек
    triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())
