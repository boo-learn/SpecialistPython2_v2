# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        side=["heads","tails"]
        self.side = random.choice(side)

coin_side=[]
n=10
for i in range(n):
    coin_=Coin()
    coin_.flip()
    coin_side.append(coin_.side)

heads_count=len([el for el in coin_side if el=="heads"])
print(coin_side)
print("Доля решек:", '{:.0%}'.format((len(coin_side)-heads_count)/len(coin_side)))
print("Доля орлов:", '{:.0%}'.format(heads_count/len(coin_side)))
