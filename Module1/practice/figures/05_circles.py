class Circle:
    def __init__(self, center_coords, radius):
        self.x0 = center_coords[0]
        self.y0 = center_coords[1]
        self.r = radius

    def intersect(self, other_circle):
        return ((self.x0 - other_circle.x0)**2 + (self.y0 - other_circle.y0)**2)**0.5 < self.r + other_circle.r


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
