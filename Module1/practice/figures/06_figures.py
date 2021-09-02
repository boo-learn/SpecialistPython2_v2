from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point3.dist_to(self.point1)
        return a + b + c

    def area(self):
        half_p = 0.5 * self.perimeter()
        return (half_p * (half_p - self.point1.dist_to(self.point2)) * (half_p - self.point2.dist_to(self.point3)) * (half_p - self.point3.dist_to(self.point1)))**0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.x0 = center_coords[0]
        self.y0 = center_coords[1]
        self.r = radius

    def area(self):
        return self.r**2 * pi


triangle1 = Triangle(Point(0, 10), Point(-8, 17), Point(9, -7))
circle1 = Circle((10, -2), 10)

figures = [triangle1, circle1]

max_area = figures[0].area()
n = 0
for i in range(1, len(figures)):
    area = figures[i].area()
    if max_area < area:
        max_area = area
        n = i

if isinstance(figures[n], Triangle):
    print('Фигура с наибольшей площадью - треугольник, площадь = ', max_area)
else:
    print('Фигура с наибольшей площадью - круг, площадь = ', max_area)
