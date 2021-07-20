import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        ch = ['heads', 'tails']
        self.side = random.choice(ch)  # random: heads/tails
        return self.side

coins = [Coin(), Coin(), Coin(), Coin(), Coin(), Coin()]
choices = [i.flip() for i in coins]

print(f"Соотношение орлов: {int(choices.count('heads') / len(choices) * 100)}%\nСоотношение решек: {int(choices.count('tails') / len(choices) * 100)}%")

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
