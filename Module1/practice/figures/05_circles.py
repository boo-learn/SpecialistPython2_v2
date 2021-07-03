class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Circle:
    def __init__(self, center_coords, radius):
        self.center_point = Point(*center_coords)
        self.radius = radius

    def intersect(self, other_circle):
        dsit_centers = self.center_point.dist_to (other_circle.center_point)
        return dsit_centers < (self.radius + other_circle.radius)


        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        ...


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
