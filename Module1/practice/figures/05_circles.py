from math import sqrt

class Circle:
    def __init__(self, center_coords, radius):
        self.tuple_koordinate = tuple(center_coords)  # получаем кортеж из координат х и у центра окружности
        self.x = self.tuple_koordinate[0]  # получаем координату х центра окружности из кортежа
        self.y = self.tuple_koordinate[1]  # получаем координату у центра окружности из кортежа
        self.rad = radius  # получаем радиус окружности

    def intersect(self, other_circle):
        """
        Проверяет пересекается ли текущая окружность с other_circle
        :return: True/False
        """
        self.dist_centre = sqrt( ((other_circle.x - self.x) ** 2) + ((other_circle.y - self.y) ** 2) )  # высчитаваем расстояние мажду центрами окружностей
        if ( (self.rad - other_circle.rad) < self.dist_centre < (self.rad + other_circle.rad) ):  # условие пересечения окружностей
            return True
        else:
            return False


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, 8), 5)  # создаем первую окружность
circle2 = Circle((2, 4), 4)  # создаем вторую окружность
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
