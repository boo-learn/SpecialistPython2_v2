import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(["head", "tail"])  # random: heads/tails


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
n = 10
coins = []
sides = []
for i in range(n):
    coins.append(Coin())  # Заполнение списка

for coin in coins:
    coin.flip()  # Подбрасываем
    sides.append(coin.side)  # Добавляем выпавшую сторону

sides_ratio = sides.count("head")/len(sides)*100

print(f' Соотношение орлов к решкам: {sides_ratio} %')
# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
