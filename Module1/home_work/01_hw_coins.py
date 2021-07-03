import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(['head', 'tail'])


if __name__ == '__main__':
    coins = [Coin()] * random.choice(range(100))
    heads = 0
    for coin in coins:
        coin.flip()
        heads += coin.side == 'head'
    print(f'Среди выпавших монеток {round(heads/len(coins), 4) * 100}%'
          f' - орлы')

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
