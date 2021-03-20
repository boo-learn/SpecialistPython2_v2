class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Метод нахождения длины отрезка по двум точкам
    def distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
zero_point = Point(0, 0)

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...
num = 0
max_length = 0
for i in range(len(points)):
    length = points[i].distance(zero_point)
    if length > max_length:
        num = i
        max_length = length

print("Координаты наиболее удаленной точки = ", points[num].x, points[num].y)
