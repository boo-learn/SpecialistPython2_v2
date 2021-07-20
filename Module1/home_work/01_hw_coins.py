import random as rnd


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        chance = rnd.randint(0, 1)
        if chance:
            self.side = 'head'  # random: heads/tails
        else:
            self.side = 'tails'
        return self.side

coins_list = [Coin().flip() for i in range(10)]

# print(sorted(coins_list))
print(f'Heads {coins_list.count("head")}, Tails: {coins_list.count("tails")}')
print(f'There are {coins_list.count("head") / coins_list.count("tails") * 100:.2f} % Heads, and {coins_list.count("tails") / coins_list.count("head") * 100:.2f} % Tails')


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
