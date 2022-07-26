class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        #если расстояние между центрами меньше либо равно сумме радиусов иначе окружности не пересекаются
        point1 = Point(self.center_coords[0], self.center_coords[1])
        point2 = Point(other_circle.center_coords[0], self.center_coords[1])
        dist = point1.dist_to(point2)
        if dist <= (self.radius + other_circle.radius):
            return True
        else:
            return False



# Окружности заданы координатами центров и радиусами
circle1 = Circle((0, 0), 5)
circle2 = Circle((10, 10), 4)

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
