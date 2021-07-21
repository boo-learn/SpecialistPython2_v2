class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def vector_sum(self, other_vector):
		self.x = self.x + other_vector.x
		self.y = self.y + other_vector.y

	def vector_difference(self, other_vector):
		self.x = self.x - other_vector.x
		self.y = self.y - other_vector.y

	def vector_scalar(self, scalar):
		self.x = self.x * scalar
		self.y = self.y * scalar
