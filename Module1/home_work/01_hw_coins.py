import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(['heads', 'tails'])  # random: heads/tails


coins = [Coin(), Coin(), Coin()]
sides = []
count = int(input('Введите целое число, сколько раз подбросить монетку: '))

for coin in coins:
    coin.flip()
    sides.append(coin.side)
print(f'Heads: {100 * sides.count("tails") / len(coins)} % '
      f'Tails: {100 * sides.count("heads") / len(coins)} %')

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip
