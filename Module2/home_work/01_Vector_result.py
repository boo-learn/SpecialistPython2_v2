class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector:({self.x},{self.y})"
    def __add__(self,vector):
        newv = Vector(self.x+vector.x,self.y+vector.y)
        return newv
    def __sub__(self,vector):
        newv = Vector(self.x-vector.x,self.y-vector.y)
        return newv
    def __mul__(self, other):
        newv = Vector(self.x*other,self.y*other)
        return newv

v1 = Vector(1,2)
v2 = Vector(2,3)
v3 = v1+v2
v4 = v1-v2
v5 = v3 * 4
print(v1,v2,v3,v4,v5)
