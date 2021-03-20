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
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point3.dist_to(self.point2)
        return a + b + c

    def area(self):
        a = self.point1.dist_to(self.point2)
        b = self.point1.dist_to(self.point3)
        c = self.point3.dist_to(self.point2)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords[0]
        self.y = center_coords[1]
        self.r = radius

    def area(self):
        return 3.1415926535 * self.r ** 2


figures = [
    Triangle(Point(0, 0), Point(0, 2), Point(2, 0)),
    Triangle(Point(0, 0), Point(0, 5), Point(5, 0)),
    Circle((0, 0), 5),
    Circle((0, 0), 15),
]

max_figure = max(figures, key=lambda f: f.area())
print(max_figure.area())


