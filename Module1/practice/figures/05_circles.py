class Circle:
    def __init__(self, center_coords, radius):
        self.center_x = center_coords[0]
        self.center_y = center_coords[1]
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist = ((self.center_x - other_circle.center_x) ** 2 + \
                (self.center_y - other_circle.center_y) ** 2) ** 0.5        
        return dist <= self.radius + other_circle.radius

    def area (self):
        import math
        return math.pi * (self.radius ** 2)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
