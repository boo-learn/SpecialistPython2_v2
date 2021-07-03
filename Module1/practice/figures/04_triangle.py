class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        return 0.5*(a + b + c)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        p = self.perimeter()
        return (p*(p-a)*(p-b)*(p-c))**0.5


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

p = triangle1.perimeter()
s = triangle1.area()

print("Периметр треугольника = ", p)
print("Площадь треугольника = ", s)
