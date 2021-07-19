class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(x_point1, y_point1, x_point2, y_point2) -> object:
    """
    Расстояние между двумя точками
    """
    result = ((x_point1 - x_point2) ** 2 + (y_point1 - y_point2) ** 2) ** 0.5
    return result

def distance_addition(points_list):
    result = []
    for i in range(len(points_list)):
        if i + 1 < len(points_list):
            result.append(distance(points_list[i].x, points_list[i].y, points_list[i + 1].x, points_list[i + 1].y))
        else:
            return result


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...

print(f'Длина ломаной линии = {sum(distance_addition(points)):.2f}')
