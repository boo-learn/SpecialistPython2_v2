import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> str:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """

        self.side = random.choice(["heads", "tails"])

n = 10
heads = 0
tails = 0
coin_list = [Coin() for i in range(n)]

for coin in coin_list:
    coin.flip()
    if coin.side == "heads": heads += 1
    else: tails += 1

print(f"heads: {heads/n*100}%  tails: {tails/n*100}%")
