class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

def section():
    section1 = ((points[0].x - points[1].x) ** 2 + (points[0].y - points[1].y) ** 2) ** 0.5
    section2 = ((points[1].x - points[2].x) ** 2 + (points[1].y - points[2].y) ** 2) ** 0.5
    section3 = ((points[2].x - points[3].x) ** 2 + (points[2].y - points[3].y) ** 2) ** 0.5
    section4 = ((points[3].x - points[4].x) ** 2 + (points[3].y - points[4].y) ** 2) ** 0.5

    return section1 + section2 + section3 + section4


# Задание: Найдите длину ломаной линии

# TODO: your core here...

print(f"Длина ломаной линии = {section()}")
