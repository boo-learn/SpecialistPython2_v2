"""
Решение Левшин Дмитрий
"""

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


n = 1000
sides = []
for i in range(n):
    coin = Coin()
    coin.flip()
    print(coin.side)
    sides.append(coin.side)

count_head = sides.count(0) * 100 / n
count_tail = sides.count(1) * 100 / n
print('Процент выпадения орла: ', count_head, "%")
print("Процент выпадения решки ", count_tail, "%")

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
