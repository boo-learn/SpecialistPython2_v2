class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

l = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
maks = 0
for i in range(len(l)-1):
    if ((l[i].x)**2 + (l[i].y)**2)**0.5 > (l[i+1].x**2 + l[i+1].y**2)**0.5:
        maks = [l[i].x,l[i].y]
    else:
        maks = [l[i+1].x,l[i+1].y]

print("Координаты наиболее удаленной точки = ", maks)
