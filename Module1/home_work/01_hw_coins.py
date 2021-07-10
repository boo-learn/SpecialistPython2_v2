# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(('heads', 'tails'))


coins_number = int(input('Введите количество монеток: '))
coins = []
for _ in range(coins_number):
    coins.append(Coin())
for coin in coins:
    coin.flip()
print(f'Процент выпавших орлов составляет - {[coin.side for coin in coins].count("heads")/coins_number*100:.0f}%')
print(f'Процент выпавших решек составляет - {[coin.side for coin in coins].count("tails")/coins_number*100:.0f}%')
