class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
class Vector:
    def __init__(self, a: Point, b:Point):
        self.a = a
        self.b = b
    def lenght(self):
        return ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5
    def __str__(self):
        return f'{self.b.x}, {self.b.y}'
    def __add__(self, vector):
        x_s = self.b.x + vector.b.x
        y_s = self.b.y + vector.b.y
        return Vector(Point(0,0),Point(x_s,y_s))
    def __sub__(self, vector):
        x_s = self.b.x - vector.b.x
        y_s = self.b.y - vector.b.y
        return Vector(Point(0,0),Point(x_s,y_s))
    def __mul__(self, mult: int):
        x_s = self.b.x * mult
        y_s = self.b.y * mult
        return Vector(Point(0,0),Point(x_s,y_s))

point1 = Point(0,0)
point2 = Point(5,0)

point3 = Point(0,0)
point4 = Point(-1,5)

vector1 = Vector(point1,point2)
vector2 = Vector(point3,point4)
vector3 = vector1 * 3

print("Sum_vector = ", vector1 + vector2)
print("Sub_vector = ", vector1 - vector2)
print(vector3)

