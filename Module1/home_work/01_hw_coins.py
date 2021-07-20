import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        if random.randint(0, 1) == 1: # random: heads/tails
            self.side = 'Tails'
        else:
            self.side = 'Heads'
        return self.side

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
coins = []
cur_coin = Coin()

coins_num = int(input('Введите целое количество испытаний:'))

for i in range(coins_num):
    coins.append(cur_coin.flip())
print('Монеты выпали сторонами:', coins)

heads_counter = 0
for i in range(len(coins)):
    if coins[i] == 'Heads':
        heads_counter += 1

heads_percent = round(heads_counter / len(coins) * 100, 1)
print('Соотношение орлов и решек:', heads_percent, '%', '/', (100 - heads_percent), '%')
