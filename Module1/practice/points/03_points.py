class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def distance(points1,points2):
    return ((points1.x -points2.x)**2 + (points1.y-points2.y)**2)**0.5

point0 = Point(0,0)
n = 0
S = 0
Q = point0
while n != len(points):
    if distance(points[n],point0)>S:
        S = distance(points[n],point0)
        Q = points[n]
        n+=1
    else:
        n+=1


print("Координаты наиболее удаленной точки = ", Q.x ,";",Q.y)
