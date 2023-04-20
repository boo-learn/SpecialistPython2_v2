import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.randint(0, 1)
        if self.side == 0:
            self.side = "Решка"
        else:
            self.side = "Орел"


n_coins = int(input("Введите количество монеток: "))
i = 0
coin_list = []

while i < n_coins:
    coin = Coin()
    coin.flip()
    coin_list.append(coin.side)
    i += 1
print(coin_list)

heads = 0
tails = 0

for _ in coin_list:
    if _ == "Орел":
        heads += 1
    elif _ == "Решка":
        tails += 1

print(f"Процентное соотношение орла к решке ровно процентов {int(heads / tails * 100)} %,"
      f" а орла к решке {int(tails / heads * 100)} %")
print(heads, tails)

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
