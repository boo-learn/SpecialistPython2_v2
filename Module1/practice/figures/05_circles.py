class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        sum_radius = self.radius + other_circle.radius
        point1 = Point(*self.center_coords)
        point2 = Point(*other_circle.center_coords)
        dist_to_centers = point1.dist_to(point2)
        return dist_to_centers < sum_radius


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print( "Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
