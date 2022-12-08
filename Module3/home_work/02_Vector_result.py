class Vector:
    
    def __init__(self, pos_a = 0, pos_b = 0) -> None:
        self.pos_a = pos_a
        self.pos_b = pos_b
        
        
    def __add__(self, other):
        foo = Vector()
        foo.pos_a = self.pos_a + other.pos_a
        foo.pos_b = self.pos_b + other.pos_b
        return f' [{foo.pos_a} , {foo.pos_b}]'
        
    def __sub__(self, other):
        foo = Vector()
        foo.pos_a = self.pos_a - other.pos_a
        foo.pos_b = self.pos_b - other.pos_b
        return f' [{foo.pos_a} , {foo.pos_b}]'
        
    def __mul__(self, num):
        foo = Vector()
        foo.pos_a = self.pos_a * num
        foo.pos_b = self.pos_b * num
        return f' [{foo.pos_a} , {foo.pos_b}]'
        
vector_one = Vector(3, 5)
vector_two = Vector(5, 4)
vector_three = Vector(2, 2)

print('vector_one + vector_two: ', vector_one + vector_two)
print('vector_two + vector_three: ', vector_two + vector_three)

print('vector_one - vector_two: ', vector_one - vector_two)
print('vector_two - vector_three: ', vector_two - vector_three)

print('vector_one * 5: ', vector_one * 5)
print('vector_two * 2: ', vector_two * 2)
