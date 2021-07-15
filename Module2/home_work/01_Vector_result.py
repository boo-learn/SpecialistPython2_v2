class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other_vector) -> tuple:
        'Summa vectorov'
        return self.x + other_vector.x, self.y + other_vector.y

    def __sub__(self, other_vector) -> tuple:
        'Raznost vectorov'
        return self.x - other_vector.x, self.y - other_vector.y

    def __mul__(self, fv_multiplicator) -> tuple:
        'Vector multiplication'
        return self.x * fv_multiplicator, self.y * fv_multiplicator



# Variables
vector_a = Vector(3, 4)
vector_b = Vector(5, 8)
multiplicator = 2

# Calculation w/ operators overloading
summa_v = vector_a + vector_b
raznost_v = vector_a - vector_b
multiplication_v = vector_a * multiplicator

# Rezult
print(f" Summ: {summa_v}, Raznost: {raznost_v}, Multiplication x{multiplicator}: {multiplication_v}")
