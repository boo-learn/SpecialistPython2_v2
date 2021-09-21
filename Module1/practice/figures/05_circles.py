class Circle:
    def __init__(self, center_coords, radius):
        self.center = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        distance_center_circle = ((self.center[0] - other_circle.center[0])
                                  ** 2 + (self.center[1] - other_circle.center[1]) ** 2) ** 0.5
        sum_radius = self.radius + other_circle.radius
        if distance_center_circle <= sum_radius:
            return True
        else:
            return False


# Окружности заданы координатами центров и радиусами
circle1 = Circle((1, -1), 1)
circle2 = Circle((1, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
