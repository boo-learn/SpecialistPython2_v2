import random


class Coin:
    HEADS = 'heads'
    TAILS = 'tails'

    def __init__(self):
        self.side = None

    def flip(self):
        self.side = random.choice([self.HEADS, self.TAILS])


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

n = 1000
count_heads = 0
count_tails = 0

coins = [Coin()] * n
for coin in coins:
    coin.flip()
    if coin.side == coin.HEADS:
        count_heads += 1
    else:
        count_tails += 1

print(f"heads: {count_heads * 100 / n}%, tails: {count_tails * 100 / n}%")
