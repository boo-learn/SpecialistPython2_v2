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
        dist_centers = self.center_coords.dist_to(other_circle.center_coords)
        return dist_centers <= self.radius + other_circle.radius and dist_centers >= abs(self.radius + other_circle.radius)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((2, 4), 2)
circle2 = Circle((2, 8), 2)


# Задание: проверьте пересекаются ли данные окружности
if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
