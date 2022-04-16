#Можно было и без точек, но так красивее мне кажется.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return f"({self.x},{self.y})"
class Vector:
    def __init__(self, dot1, dot2):
        self.a = dot2.x - dot1.x
        self.b = dot2.y - dot1.y
    def show(self):
        return f"({self.a},{self.b})"

    def sum_v(self, vec1):
        return Vector(Point(0,0), Point(self.a + vec1.a, self.b + vec1.b))
    def sub_v(self, vec1):
        return Vector(Point(0, 0), Point(self.a - vec1.a, self.b - vec1.b))
    def mul_v(self, mult):
        return Vector(Point(0, 0), Point(self.a*mult, self.b*mult))

A = Point(2,4)
B = Point(5,8)
C = Point(6,3)
AB = Vector(A, B)
AC = Vector(A, C)
k = 3
print(f"AB {AB.show()}")
print(f"AC {AC.show()}")
print(f"AB+AC {Vector.sum_v(AB,AC).show()}")
print(f"AB-AC {Vector.sub_v(AB,AC).show()}")
print(f"AB*k {Vector.mul_v(AB,k).show()}")
