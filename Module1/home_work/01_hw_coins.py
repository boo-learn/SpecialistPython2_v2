import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.randint(1, 2)  # random: heads/tails
        if self.side == 1:
            self.side = "heads"
        elif self.side == 2:
            self.side = "tails"
        return self.side


n = int(input("Введите кол-во монет >"))
coins = []
res = []
heads = 0
tails = 0
for i in range(n):
    coins.append(Coin())

for i in range(n):
    res.append(coins[i].flip())
    if coins[i].flip() == "heads":
        heads += 1
    elif coins[i].flip() == "tails":
        tails += 1
print(f"Процент орлов : {round(heads/n,2)}, Процент решек:{round(tails/n,2)})")

