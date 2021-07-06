import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """

        self.side = flip_coin


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

coins_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heads_count = 0
tails_count = 0
for coin in coins_list:
    coin_var = ['heads', 'tails']
    flip_coin = random.choice(coin_var)
    if flip_coin == 'heads':
        heads_count += 1
    else:
        tails_count += 1
    print(flip_coin)
ratio_heads = heads_count / (heads_count + tails_count) * 100
ratio_tails = 100 - ratio_heads
print(heads_count, tails_count)
print("Процент выпавших орлов ", ratio_heads, "%")
print("Процент выпавших решек ", ratio_tails, "%")
