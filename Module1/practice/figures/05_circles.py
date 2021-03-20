class Circle:
    def __init__(self, center_coords, radius):
        self.x = center_coords[0]
        self.y = center_coords[1]
        self.r = radius

    def intersect(self, other_circle):
        centers_dist = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
        if centers_dist > self.r + other_circle.r:
            return False
        else:
            return True

# Окружности заданы координатами центров и радиусами
circle1 = Circle((0, 0), 5)
circle2 = Circle((0, 9), 3)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
