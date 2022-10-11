import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])

n = int(input("enter the # of coins"))
coinlist =[]
heads = 0
tails = 0

for i in range(n):
    coin = Coin()
    coinlist.append(coin)

for i in range(n):
    coinlist[i].flip()
    print(coinlist[i].side)

    if coin.side == 'heads':
        heads += 1
    elif coin.side == 'tails':
        tails += 1

print("Tails = ", tails/n*100, "%")
print("Heads = ", heads/n*100, "%")