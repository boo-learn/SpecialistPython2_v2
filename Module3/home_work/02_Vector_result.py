
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = (x**2+y**2)**0.5

    def addtn(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def substr(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def mult_scal(self, scal):
        return Vector(self.x*scal, self.y*scal)



vec1 = Vector(1, 2)
vec2 = Vector(2, 1)
vec3 = vec1.addtn(vec2)
print(vec3.x, vec3.y, vec3.a)
vec4 = vec3.substr(vec2)
print(vec4.x, vec4.y, vec4.a)
vec5 = vec4.mult_scal(2)
print(vec5.x, vec5.y, vec5.a)

