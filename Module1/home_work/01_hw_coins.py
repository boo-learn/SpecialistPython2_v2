coins = [1,2,3,4,5,6,78]


import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None


    def flip(self):
        heads = 0
        tails = 0
        for coin in coins:
            random.seed(coin)
            side = random.random()
            if side >= 0.5:
                heads+=1
            if side <  0.5:
                tails+=1
        print('соотношение:', ((heads*100)/(heads+tails)))

Coin.flip(coins)
