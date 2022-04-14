class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        # TODO-1: реализуйте метод
        return ((self.center_coords[0]-other_circle.center_coords[0])**2 + (self.center_coords[1]-other_circle.center_coords[1])**2)**0.5 <= (self.radius+other_circle.radius)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)


if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
