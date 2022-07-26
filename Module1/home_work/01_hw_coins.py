import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = 'head' if random.randint(0, 1) == 0 else 'tails'  # random: heads/tails


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

coins = []
n = random.randint(5, 10)
for i in range(n):
    coins.append(Coin())
cnt_tails = 0
cnt_heads = 0
for coin in coins:
    coin.flip()
    if coin.side == "tails":
        cnt_tails += 1
    else:
        cnt_heads += 1
print(f"Процент tails = {round(cnt_tails/n,2)} heads = {round(cnt_heads/n,2)}")


