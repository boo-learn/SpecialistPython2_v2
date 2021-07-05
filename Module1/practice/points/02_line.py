class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def crocked_line_length(points_list: list):
    line_len = 0
    for i in range(1, len(points_list)):
        line_len += ((points_list[i].x - points_list[i - 1].x)**2 + (points_list[i].y - points_list[i - 1].y)**2)**0.5
    return line_len


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]


# Задание: Найдите длину ломаной линии

# TODO: your core here...

print("Длина ломаной линии = ", crocked_line_length(points))
