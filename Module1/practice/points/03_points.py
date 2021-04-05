class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

def dist(p1, p2):
    return ((p2.x-p1.x)**2 + (p2.y-p1.y)**2)**0.5

a=Point(0,0)
d=0
for i in points:
    dl=dist(i,a)
    if dl>d:
        d=dl
    
    
print("Координаты наиболее удаленной точки = ", d)
