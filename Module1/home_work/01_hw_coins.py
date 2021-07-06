import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = ...  # random: heads/tails


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
        self.side = ...  # random: heads/tails
        sides = ['tails','heads']
        return random.choice(sides)# Подбрасывание монетки


n = 100
coins = []
for i in range(n):
    coins.append(Coin())
numb_heads = 0
numb_tails = 0

coin_list = []
for coin in coins:
    if  coin.flip == "tails":
        numb_tails += 1
    else:
        numb_heads += 1
print (f"решка: {numb_tails/n*100} орел: {numb_heads/n*100} ")
