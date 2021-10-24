class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_len = 0
target_point=points[0]
for point in points:
    dist=((point.x)**2+(point.y)**2)**0.5
    if dist>max_len:
        target_point=point

print("Координаты наиболее удаленной точки = ", target_point.x,target_point.y)
