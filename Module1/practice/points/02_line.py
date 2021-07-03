l = 0 #длина ломаной

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]


def distance(p1, p2): #функция для нахождения расстояния между точками
    dist = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
    return dist


lenp = (len(points))  #находит сколько элементов в списке
a = 0
while a < (lenp-1):
    l += distance(points[a], points[a+1])
    a+=1
print (l)
