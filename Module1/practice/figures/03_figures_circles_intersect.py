class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Circle:
    def __init__(self, center_coords, radius):
        self.center = Point(*(center_coords))
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        # TODO-1: реализуйте метод
        return self.center.dist_to(other_circle.center) <= self.radius + other_circle.radius


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 15)
circle2 = Circle((13, -8), 4)

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")

