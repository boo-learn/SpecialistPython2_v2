import math


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def get_length(self) -> float:
        """
        :return: длину окружности
        """
        return 2 * math.pi * self.radius

    def get_area(self) -> float:
        """
        :return: площадь окружности
        """
        return math.pi * self.radius ** 2


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

print(f"Длина окружности радиусом {circle1.radius} = {circle1.get_length()}")
print(f"Длина окружности радиусом {circle2.radius} = {circle2.get_length()}")

print(f"Площадь окружности радиусом {circle1.radius} = {circle1.get_area()}")
print(f"Площадь окружности радиусом {circle2.radius} = {circle2.get_area()}")
