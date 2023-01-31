import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.randint(0, 1)

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах
coin1 = Coin()

coins_number = int(input('Enter coins number: '))
side_heads = 0
side_tails = 0

for i in range(coins_number):
    side_int = coin1.flip()
    side_int = coin1.side

    if side_int == 0:
        side_heads += 1
    else:
        side_tails += 1

print('Coins with heads is ' + str(side_heads) + '.')
print('Coins with tails is ' + str(side_tails) + '.')


# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
