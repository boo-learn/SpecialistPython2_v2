import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = 'heads' if random.random() >= 0.5 else 'tails' # random: heads/tails

# Число монеток
nunCoin = 100

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
coins = [Coin() for _ in range(nunCoin)]
for coin in coins:
    coin.flip()

# выведите соотношение выпавших орлов и решек в процентах
countHeads = 0
for coin in coins:
    if coin.side == 'heads':
        countHeads += 1

print(f'Процентное соотношение орлов {countHeads / nunCoin * 100:.1f}%')
print(f'Процентное соотношение решек {(nunCoin - countHeads) / nunCoin * 100:.1f}%')
