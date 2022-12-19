import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])  # random: heads/tails


if __name__ == "__main__":
    n = 15000
    #n = int(input())
    # 1. Создайте список из n-монеток, n - вводится с клавиатуры:
    coins = [Coin() for i in range(n)]
    # 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip():
    for coin in coins:
        coin.flip()
    # 3. Выведите соотношение выпавших орлов и решек в процентах:
    heads_count = [coin.side for coin in coins].count('heads')
    heads_percent = (heads_count / n) * 100
    tails_percent = 100 - heads_percent
    print(f"Орлы: {heads_percent:.2f}%, решки: {tails_percent:.2f}%")

