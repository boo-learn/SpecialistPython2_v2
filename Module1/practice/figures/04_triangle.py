class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + \
                (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        per = self.point1.dist_to(self.point2)
        per += self.point2.dist_to(self.point3)
        per += self.point3.dist_to(self.point1)
        return per
        

    def area(self):
        lines = [self.point1.dist_to(self.point2),
                 self.point2.dist_to(self.point3),
                 self.point3.dist_to(self.point1)]
        half_per = self.perimeter() / 2        
        area = (half_per * (half_per - lines[0]) * (half_per - lines[1]) * \
        (half_per - lines[2])) ** 0.5        
        return area


# Треугольник задан координатами трех точек
triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 0))
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...

print("Периметр треугольника = ", round(triangle1.perimeter(), 2))
print("Площадь треугольника = ", round(triangle1.area(), 2))
