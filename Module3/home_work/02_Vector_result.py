class MyVector:
    def __init__(self, x:float = 0, y: float = 0):
        if type(x)==int or float:
            self.x=x
        if type(y) == int or float:
            self.y=y

    def __add__(self, other_vec):
        return MyVector(self.x + other_vec.x, self.y + other_vec.y)
    def __mul__(self, scal):
        return MyVector(self.x * scal, self.y*scal)
    def __sub__(self, other_vec):
        return MyVector(self.x + other_vec.x*(-1), self.y + other_vec.y*(-1))

vec1=MyVector(1,1)
vec2=MyVector(1,1)
vac3 = vec1-vec2
print(vac3.x, vac3.y)
