import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        if random.randint(0,1)==0:
            self.side = "heads"  # random: heads/tails
        else:
            self.side = "tails"
n=10
heads=0
tails=0
coinlist=[]
for i in range(n):
    coinlist.append(Coin())
    print(i)

for coin in coinlist:
    coin.flip()
    if coin.side=="heads":
        heads=heads+1
    else:
        tails=tails+1
proc=heads/tails*100
print(f"соотношение выпавших орлов и решек в процентах: {proc} ")
