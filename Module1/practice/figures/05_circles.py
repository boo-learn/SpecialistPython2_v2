def distance(point1, point2):
    a = (((point2.x-point1.x)**2 + (point2.y - point1.y))**2)**0.5
    return a

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        dist = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return dist

class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = Point(*center_coords)
        self.radius = radius


    def intersect(self, other_circle):
        rad_dict = self.center_coords.dist_to(other_circle.center_coords)
        radius_sum = self.radius + other_circle.radius
        if rad_dict < radius_sum:
            return False
        else:
            return True


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
