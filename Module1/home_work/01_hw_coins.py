import random


class Coin:
	def __init__(self):
		# heads-орел/tails-решка
		self.side = None

	def flip(self):  # Подбрасывание монетки
		self.side = random.choice(['heads', 'tails'])


n = random.randint(1, 50)

heads = 0
tails = 0
c = 0
for c in range(n):
	x = Coin()
	x.flip()
	if x.side == 'heads':
		heads += 1
	elif x.side == 'tails':
		tails += 1

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

print(f'coins random created: {n}\nheads: {round(heads / n * 100)}%\ntails: {round(tails / n * 100)}%')
