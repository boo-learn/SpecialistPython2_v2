import random


class Coin:
    def __init__(self, side):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        sides = ["head", "tail"]
        self.side = random.choice(sides)
        # random: heads/tails


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

coins = []
n = random.randint(100, 1000)
for i in range(n):
    coins.append(Coin(None))

for coin in coins:
    coin.flip()

side_head=0
for coin in coins:
    if coin.side=="head":
        side_head+=1

print(f"процент выпавших орлов: {side_head/n*100} \n"
      f"процент выпавших решек: {(n-side_head)/n*100}")
