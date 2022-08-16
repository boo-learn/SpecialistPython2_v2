import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        self.side = random.choice(('heads', 'tails'))


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

n = 1000
coins = []
heads = 0
tails = 0

for i in range(n):
    coins.append(Coin())
    coins[i].flip()
    if coins[i].side == 'heads':
        heads += 1
    else:
        tails += 1

tails_percent = tails / (heads + tails) * 100
heads_percent = heads / (heads + tails) * 100
print(f"Решки {tails_percent:.1f}%     Орлы {heads_percent:.1f}%")
