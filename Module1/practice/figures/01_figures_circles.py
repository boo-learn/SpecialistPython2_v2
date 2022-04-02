from math import pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center_coords, radius):
        self.center = Point(*(center_coords))
        self.radius = radius

    def length(self):
        """
        :return: длину окружности
        """
        return 2 * pi * self.radius

    def area(self):
        """
        :return: площадь окружности
        """
        return pi * (self.radius) ** 2


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

print(f"Длина окружности радиусом {circle1.radius} = {circle1.length()}")
print(f"Длина окружности радиусом {circle2.radius} = {circle2.length()}")

print(f"Площадь окружности радиусом {circle1.radius} = {circle1.area()}")
print(f"Площадь окружности радиусом {circle2.radius} = {circle2.area()}")
