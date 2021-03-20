class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = ((self.center_coords[0] - other_circle.center_coords[0]) ** 2 + (self.center_coords[1] - other_circle.center_coords[1]) ** 2) ** 0.5
        if d > self.radius + other_circle.radius or d < abs(self.radius - other_circle.radius):
            return False
        else:
            return True


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
