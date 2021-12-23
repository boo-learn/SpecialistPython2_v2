# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
        # heads-орел/tails-решка
import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        self.side = random.choice(['heads', 'tails'])
        return self.side == 'heads'

list_coin = [Coin(), Coin(), Coin(), Coin(), Coin(), \
             Coin(), Coin(), Coin(), Coin(), Coin()]
heads = 0
for coin in list_coin:
    if coin.flip():
        heads += 1
result_heads = 100 / len(list_coin) * heads
result_tails = 100 - result_heads

print(f'Выпавших орлов: {result_heads}%\nВыпавших решек : {result_tails}%.')
