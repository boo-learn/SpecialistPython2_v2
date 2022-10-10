import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        sides = ["heads", "tails"]
        self.side = random.choice(sides)  # random: heads/tails

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

n = int(input("Количество монеток: "))
coins = [Coin] * n
heads = 0
tails = 0
for coin in coins:
    coin.flip(coin)
    if coin.side == "heads":
        heads += 1
    else:
        tails += 1
print(int(heads/n*100), '%')
print(int(tails/n*100), '%')


# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
