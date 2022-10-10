import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(["heads","tails"])
        
try:
    n = int(input("Введите число монет: "))
    heads = 0
    tails = 0
    coins = [Coin() for x in range(n)]
    for coin in coins:
        coin.flip()
        if coin.side == "heads":
            heads += 1
        else:
            tails += 1
    print(f" Из {n} Пподброшенных монет процент орлов составляет: {heads / n * 100} %, процент решек: {tails / n * 100} %")
except Exception as e:
    print('Неверный формат вводимого числа')
