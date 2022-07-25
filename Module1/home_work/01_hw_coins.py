import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(["head","tail"])  # random: heads/tails

n = 50

coins = [Coin() for idx in range(n)]

for coin in coins:
    coin.flip()

heads_count = len([item for item in coins if item.side == "head"])
tails_count = len([item for item in coins if item.side == "tail"])

print("Всего монеток {count}. Орел - {heads}%. Решка - {tails}% ".format(count = n, heads =heads_count/n *100, tails = tails_count /n *100))

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
