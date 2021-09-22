### учтен момент с одинкаковыми координатами центра окружностей
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        # self.center = Point(center_coords[0], center_coords[1])
        self.center = Point(*center_coords)
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        dist_centers = self.center.dist_to(other_circle.center)
        ### учтено что одна окружность может быть внутри другой целиком
        return (dist_centers <= self.radius + other_circle.radius and dist_centers != 0) or \
               (dist_centers == 0 and self.radius == other_circle.radius)

# Окружности заданы координатами центров и радиусами
circle1 = Circle((10, -8), 5)
circle2 = Circle((10, -8), 5)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
