import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(["heads", "tails"])  # random: heads/tails

n = int(input())
head = 0
tail = 0
list_coins = [Coin() for x in range(n)]
for coin in list_coins:
    coin.flip()
    if coin.side == "heads":
        head += 1
    else:
        tail += 1
print(f" {head / (head + tail) * 100}% орлов и {tail / (head + tail) * 100}% решек")


# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
