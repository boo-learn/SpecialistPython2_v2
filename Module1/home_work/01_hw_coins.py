
import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = ['heads', 'tails']        # random: heads/tails
        return random.choice(self.side)

coins_list = []
n = int(input('Сколько монеток Вы хотите подбросить? '))
for i in range(n):
    coins_list.append(Coin())

choice = []
for coin in coins_list:
    choice.append(coin.flip())

heads_num = choice.count('heads') * 100 / n
tails_num = choice.count('tails') * 100 / n

print(f'Соотношение выпавших орлов и решек {heads_num} % к {tails_num} %.')
