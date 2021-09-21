import random

class Coin:
    def __init__(self, x, y):
        # heads-орел/tails-решка
        self.head = x
        self.tails = y

def flip():
    return random.randint(0, 1)

n = 10
coin_flip_res = []
for i in range(n):
    if flip() == 0:
        coin_flip_res.append("head")
    else:
        coin_flip_res.append("tails")
print(coin_flip_res)

heads = 0
tails = 0
for el in coin_flip_res:
    if el == "head":
        heads+=1
    else:
        tails+=1
heads_ratio = heads / (heads+tails)*100
tails_ratio = tails / (heads+tails)*100

print(f"Number of heads: {heads}, Number of tails: {tails}")
print(f"Heads ratio: {heads_ratio} %, Tails ratio: {tails_ratio} %")

