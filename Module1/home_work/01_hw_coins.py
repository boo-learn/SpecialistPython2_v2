import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        if random.randint(0, 1) == 0:
            self.side = 'heads'
        else:
            self.side = 'tails'


n = 10
coins = [Coin()]*n
count_all = 0
count_heads = 0

for coin in coins:
    count_all += 1
    coinFlip = coin.flip()
    if coin.side == 'heads':
        count_heads += 1
print(
    f'Доля орлов: {count_heads/count_all*100}, доля решек: {(count_all-count_heads)/count_all*100}'
)
