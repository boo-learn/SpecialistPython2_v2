class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords[0]
        self.y = center_coords[1]
        self.rad = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
        if dist > self.rad + other_circle.rad:
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
