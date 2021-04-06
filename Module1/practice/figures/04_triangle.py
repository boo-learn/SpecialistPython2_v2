class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
    	return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self, point1, point2, point3):
        return (point1.dist_to(point2) + point2.dist_to(point3) + point3.dist_to(point1))

    def area(self, point1, point2, point3):
        a = point1.dist_to(point2)
        b = point2.dist_to(point3)
        c = point1.dist_to(point3)
        p = (a + b + c) / 2
        ar = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return ar


triangle1 = Triangle(Point(2, 4), Point(6, 8), Point(-2, 0))

perim = triangle1.perimeter(Point(2, 4), Point(6, 8), Point(-2, 0))
are = triangle1.area(Point(2, 4), Point(6, 8), Point(-2, 0))

print("Периметр треугольника = ", perim)
print("Площадь треугольника = ", are)
