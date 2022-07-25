import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        return round (random.random())

number = int(input("Enter the number of coins to toss "))
tails = 0
i = 0

for i in range(0, number):
    res = Coin.flip(i)
    if res == 0:
        tails += 1

print(f"Distribution of heads and tails is  {(number - tails) / number: .2%} to {tails / number: .2%}")


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
