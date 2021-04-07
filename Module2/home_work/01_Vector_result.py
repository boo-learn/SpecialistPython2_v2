class Vector:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __add__(self, other_v):
		return (self.x + other_v.x , self.y + other_v.y)
		
	def __sub__(self, other_v):
		return (self.x - other_v.x , self.y - other_v.y)
		
	def __mul__(self, sc):
		return (self.x * sc, self.y * sc)
	
vector1 = Vector(2, 4)
vector2 = Vector(-7, 1)

print(f'Сумма векторов равна {vector1 + vector2}')

print(f'Разница векторов равна {vector1 - vector2}')
print(f'Прозведение вектора1 и числа 3 равно {vector1 * 3}')
