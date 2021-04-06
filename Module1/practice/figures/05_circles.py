from math import sqrt


class Point:
    """Точка в двоичной системе координат"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        """Расстояние между двумя точками"""
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


class Circle:
    """Окружность по координатам центра и радиусу"""
    def __init__(self, center_coords: Point, radius: float):
        self.center_coords = center_coords
        self.radius = radius

    def intersect(self, other_circle) -> bool:
        """Проверяет пересекается ли текущая окружность с окружностью other_circle"""
        radii = [self.radius, other_circle.radius]  # оказывается радиус в множественном числе - это radii
        dist = self.center_coords.dist_to(other_circle.center_coords)
        if dist > sum(radii) or dist < min(radii):
            return False
        else:
            return True


if __name__ == '__main__':
    # Окружности заданы координатами центров и радиусами
    circle1 = Circle(Point(6, -8), 5)
    circle2 = Circle(Point(2, 4), 4)

    # Задание: проверьте пересекаются ли данные окружности
    if circle1.intersect(circle2):
        print("Окружности пересекаются")
    else:
        print("Окружности НЕ пересекаются")

    circle3 = Circle(Point(0, 0), 1)
    circle4 = Circle(Point(0, 2), 1)

    if circle3.intersect(circle4):
        print("Окружности пересекаются")
    else:
        print("Окружности НЕ пересекаются")
