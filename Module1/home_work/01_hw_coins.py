import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        self.side = random.choice(['heads', 'tails'])

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

def flip_coins(n):
    wallet = [Coin() for _ in range(n)]
    heads = 0
    tails = 0

    for coin in wallet:
        coin.flip()
        if coin.side == 'heads':
            heads += 1
        elif coin.side == 'tails':
            tails += 1
            
    return heads / n * 100, tails / n * 100

heads, tails = flip_coins(1000)

print(f'Количество орлов: {heads:.2f} %')
print(f'Количество решек: {tails:.2f} %')
