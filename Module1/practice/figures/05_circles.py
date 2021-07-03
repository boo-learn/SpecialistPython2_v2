class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords[0]
        self.y = center_coords[1]
        self.radius = radius

    def intersect(self, other_circle):
        l = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
        return l <= self.radius + other_circle.radius


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
