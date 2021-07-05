class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1:Point,p2:Point):
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
len_max = 0
i = 0

while i<len(points)-1:
    point1 = points[i]
    point2 = points[i+1]
    dist = distance(point1,point2)
    if dist > len_max:
        len_max = dist
    i += 1
print("Координаты наиболее удаленной точки = ", len_max)
