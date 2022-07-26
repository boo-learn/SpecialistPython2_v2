import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.coin_stat = None
        self.side = None
        self.heads_cnt = 0
        self.tails_cnt = 0

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.randint(0, 1)  # random: heads/tails
        if self.side == 0:
            self.heads_cnt += 1
        else:
            self.tails_cnt += 1
        self.coin_stat = {"орел": self.heads_cnt / (self.heads_cnt + self.tails_cnt) * 100,
                          "решка": self.tails_cnt / (self.heads_cnt + self.tails_cnt) * 100
                          }


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах
num_coins = int(input("Сколько монеток подкинуть? "))
coins = [Coin() for el in range(num_coins)]  # список из монеток
for coin in coins:
    coin.flip()  # подбрасываем каждую монетку
    print(coin.side, end=" ")
heads_cnt = len([coin.side for coin in coins if coin.side == 0])  # количество орлов
tails_cnt = len([coin.side for coin in coins if coin.side == 1])  # количество решек
print(f"\nорлов: {heads_cnt}, решек: {tails_cnt}")
try:
    print(f"орел: {heads_cnt / (heads_cnt + tails_cnt) * 100:.2f}%"
          f"\nрешка: {tails_cnt / (heads_cnt + tails_cnt) * 100:.2f}% ")
except ZeroDivisionError:
    print("Нужна хотя бы 1 монета")

# Это другой вариант решения. Он не совсем соответствуют тексту задания, но считает то же самое
print("========\n\nВариант решения2:\n"
      "[Одну монетку подкидываем несколько раз]")
my_coin = Coin()
num_flips = int(input("Сколько раз подкинуть? "))
while num_flips > 0:
    my_coin.flip()
    print(my_coin.side, end=" ")
    num_flips -= 1
try:
    print(f"\nорел: {my_coin.coin_stat['орел']:.2f}%"
          f"\nрешка: {my_coin.coin_stat['решка']:.2f}%")
except TypeError:
    print("Нужно подкинуть хотя бы 1 раз")
