import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.randint(0, 1)
        return 'heads' if self.side == 0 else 'tails'


coins = [Coin(), Coin(), Coin(), Coin(), Coin()]

count_heads = 0
count_tails = 0
for el in coins:
    if el.flip() == 'heads':
        count_heads += 1
    else:
        count_tails += 1

print(f'{count_heads / len(coins) * 100 }% heads and {count_tails / len(coins) * 100}% tails')

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
