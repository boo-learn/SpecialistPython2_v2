import math


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def length(self):
        """
        :return: длину окружности
        """
        return self.radius * 2 * math.pi

    def area(self):
        """
        :return: площадь окружности
        """
        return self.radius ** 2 * math.pi


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

print(f"Длина окружности радиусом {circle1.radius} = {circle1.length()}")
print(f"Длина окружности радиусом {circle2.radius} = {circle2.length()}")

print(f"Площадь окружности радиусом {circle1.radius} = {circle1.area()}")
print(f"Площадь окружности радиусом {circle2.radius} = {circle2.area()}")
