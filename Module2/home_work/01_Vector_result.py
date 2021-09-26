class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def subtraction(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def multiplication(self, scalyar):
        if scalyar >= 0:
            return Vector(self.x * scalyar, self.y * scalyar)
        else:
            return Vector(self.y * scalyar, self.x * scalyar)

    def __str__(self):
        return f'{self.x}, {self.y}'


vector1 = Vector(5, 7)
vector2 = Vector(12, 9)
vector3 = Vector(-2, -5)

if __name__ == '__main__':
    print(f'vector1 = {vector1}')
    print(f'vector2 = {vector3}')
    print(f'vector3 = {vector2}')

    print(f'vector1 + vector2 = {vector1.addition(vector2)}')
    print(f'vector2 + vector3 = {vector2.addition(vector3)}')
    print(f'vector2 - vector1 = {vector1.subtraction(vector2)}')
    print(f'vector3 - vector1 = {vector3.subtraction(vector1)}')
    print(f'vector3 * scalyar = {vector3.multiplication(4)}')
    print(f'vector2 * scalyar = {vector2.multiplication(12)}')
    print(f'vector1 * scalyar = {vector1.multiplication(-5)}')
