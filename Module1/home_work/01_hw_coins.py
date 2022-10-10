import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(["heads", "tails"])

    # def show(self) -> str:
    #     return f"{self.side}"

        # random: heads/tails
n = int(input())
Coins = []
for i in range(n):
    Coins.append(Coin())

countHead = 0
for coin in Coins:
    coin.flip()
    if coin.side == "heads":
        countHead += 1
    # print(coin.show())

print(f' {round(countHead / n * 100, 2)}% орлов {round((1 -countHead / n) * 100, 2)}% решек')
