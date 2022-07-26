import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(["heads","tails"])



coins = [Coin(), Coin(), Coin(), Coin(), Coin(),Coin()]
side_heads = 0
side_tails = 0
for coin in coins:
    coin.flip()
    # print(coin.side)
    if coin.side == "heads":
        side_heads = side_heads + 1
    else:
        side_tails = side_tails + 1
# print(side_heads," ",side_tails)
print(side_heads/(side_heads + side_tails)*100,"% орлов ",side_tails/(side_heads + side_tails)*100,"% решек")

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
