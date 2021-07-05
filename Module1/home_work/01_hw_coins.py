import random


class Coin:

    def __init__(self):
        # heads-орел/tails-решка
        self.side = None


    def flip(self):
        sides = ['heads', 'tails']

        self.side = random.choice(sides)  # random: heads/tails
        return self.side


num_coins = 10
coins = []
while num_coins > 0:
    coins.append(Coin())
    num_coins -= 1

sides_coins = []
for coin in coins:
    sides_coins.append(coin.flip())
print(sides_coins)
heads = 0
tails = 0
for side in sides_coins:
    if side == 'heads':
        heads += 1
    else:
        tails += 1
print(heads, tails)
print(f'Соотношение heads к tails: {heads/len(coins)*100}% к {tails/len(coins)*100}%')
