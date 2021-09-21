class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = Point(*center_coords) 
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = self.center_coords.dist_to(other_circle.center_coords)
        return self.radius + other_circle.radius <= dist




# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
