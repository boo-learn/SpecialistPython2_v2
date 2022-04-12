class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center_coords, radius):
        ...

    def point_into(self, point):
        """
        Проверяет лежит ли точка point внутри текущей окружности
        :return: True/False
        """
        # TODO-1: реализуйте метод
        ...


# Окружность задана координатами центра и радиусом:
circle1 = Circle((6, -8), 10)
# И дана точка:
point1 = Point(7, 1)

if circle1.point_into(point1):
    print(f"Точка лежит внутри окружности")
else:
    print("Точка НЕ лежит внутри окружности")