class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        sum_radius = self.radius + other_circle.radius
        point1 = Point(*self.center_coords)
        point2 = Point(*other_circle.center_coords)
        dist_to_centers = point1.dist_to(point2)
        return dist_to_centers < sum_radius

    def area(self):
        return 3.14 * self.radius**2


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
        return (p*(p - a)*(p - b)*(p - c)) ** 0.5


circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))

print(max(circle1.area(), circle2.area(), triangle1.area()))
