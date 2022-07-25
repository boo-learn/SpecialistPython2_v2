import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(['Head','Tails'])
        return self.side
n=10

coins = [Coin().flip() for i in range(n)]
# for coin in coins:
#     Coin.flip()
print ("Head to Tails is: ", coins.count('Head')/coins.count('Tails'))
