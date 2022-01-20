class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a= 0
l = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

for i in range(len(l)-1):
    a = a + ((l[i].x - l[(i+1)].x)**2 + (l[i].y - l[(i+1)].y))**0.5

print("Длина ломаной линии = ",a)
