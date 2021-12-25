import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        self.side = random.randint(0,1)
        if self.side == 0:
            return 'head'
        else:
            return 'tails'
heads = []
tails = []
coins = [Coin(),Coin(),Coin(),Coin()]
for i in coins:
    a = i.flip()
    if a == 'head':
        heads.append(a)
    else:
        tails.append(a)
print(len(heads)/len(tails))
