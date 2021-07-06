import random


class Coin:
    '''
    Класс монета
    '''
    sides = {1: "heads", 0: "tails"}

    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = self.sides[random.randint(0, 1)]


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
wallet = [Coin() for coin in range(random.randint(10, 50))]
heads_counter = 0
for coin in wallet:
    coin.flip()
    if coin.side == "heads":
        heads_counter += 1

print(f'Доля выпавших орлов {heads_counter/len(wallet)}.\nДоля выпавших решек '
      f'{1 - heads_counter/len(wallet)}.\nВсего монет {len(wallet)}.')
