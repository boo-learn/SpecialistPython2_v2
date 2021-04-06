import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = ''
        self.flip()     # Generating 'self.side' attribute

    def __str__(self):
        return f'Coin: {self.side=}'

    def __repr__(self):
        return self.__str__()

    def flip(self):
        """Подбрасывание монетки"""
        sides = ['heads', 'tails']
        self.side = random.choice(sides)


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

if __name__ == '__main__':
    coins = []
    for coin in range(0, 1000):
        coins.append(Coin())
    count = len(coins)
    heads = len(list(filter(lambda x: x.side == 'heads', coins)))
    tails = len(list(filter(lambda x: x.side == 'tails', coins)))
    print(f'Всего было подброшено {count} монет, из них {heads} ({round((heads / count * 100), 2)}%) орлов '
          f'и соответственно {tails} ({round((tails / count * 100), 2)}%) решек')
