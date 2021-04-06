# Баранова Ксения

import random

class Coin:
    def __init__(self):
    	self.side = None       

    def flip(self):
    	self.side = random.randint(0 ,1)
    	return self.side

n = int(input('Введите количество монет: '))
coins = [Coin()] * n

heads = 0
tails = 0
for coin in coins:
	coin.flip()
	if coin.flip() == 1:
		heads += 1
	else:
		tails += 1

print(f'Орел выпал в {round(heads / n * 100)}% случаев , а  решка - в {round(tails / n * 100)}%')
