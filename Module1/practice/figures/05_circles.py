class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point x:{self.x}, y:{self.y}"

    def dist_to(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.cc = Point(*center_coords)
        self.rad = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = self.cc.dist_to(other_circle.cc)
        return (self.rad - other_circle.rad) < dist < (self.rad + other_circle.rad)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
