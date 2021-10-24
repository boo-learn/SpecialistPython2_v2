class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    dist = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**0.5
    return dist
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
new_points=[]
for i in range(len(points)):
    if (i+1)<len(points):
        new_points.append(distance(points[i],points[i+1]))

print(f"Координаты наиболее удаленной точки = {max(new_points)}")
