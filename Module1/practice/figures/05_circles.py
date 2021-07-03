class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def leng(p1, p2):
        """
        Расстояние между двумя точками
        """
        #     x1-x2**2 + y1-y2**2
        return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
        

class Circle:
    def __init__(self, center_coord, radius):
        self.center = Point(*center_coord)
        self.radius = radius


    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        d = self.center.leng(other_circle.center)

        return d < (self.radius + other_circle.radius)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
