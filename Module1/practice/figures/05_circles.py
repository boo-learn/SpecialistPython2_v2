class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'Point ({self.x, self.y, self.color})'

    def dist_to(self, other_point):
        return round(((self.x - other_point.x) ** 2 +
                      (self.y - other_point.y) ** 2) ** 0.5, 2)


class Circle:
    def __init__(self, center_coords, radius):
        self.center = Point(*center_coords)
        self.radius = radius

    def intersect(self, other_circle) -> bool:
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = self.center.dist_to(other_circle.center)
        return d < (self.radius + other_circle.radius)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
