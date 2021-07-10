import random
import random, sys
'''
Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
выведите соотношение выпавших орлов и решек в процентах
'''


class Coin:
    HEAD = "Head"
    TAIL = "Tail"

    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = ...  # random: heads/tails
        self.side = random.choice([Coin.HEAD, Coin.TAIL])
        if self.side == Coin.HEAD:
            return True

    def to_str(self, ind):
        return f"Coin#{ind}: {self.side}"


try:
    coin_count = int(input('Введите кол-во монет: '))
    if coin_count <= 0:
        sys.exit(1)
except:
    print("Error: Integer and gt 0")
    sys.exit(1)


coin_ind = 0
coin_head_count = 0
for coinN in range(coin_count):
    coinN = Coin()
    if coinN.flip():
        coin_head_count += 1
    coin_ind += 1

head_per = round(coin_head_count / coin_count * 100, 2)
tail_per = round(100 - head_per, 2)


print("Доля решек: ", tail_per, "%")
print("Доля орлов: ", head_per, "%")
