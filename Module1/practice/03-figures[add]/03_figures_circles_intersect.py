class Circle:
    def __init__(self, center_coords, radius):
        ...

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        # TODO-1: реализуйте метод
        ...


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
