import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self, i):
        self.side = i

    def get_side(self):
        return self.side


n = 10
mas_coin = []
mas_side = ["heads", "tails"]
counter = 0
for i in range(n):
    a = Coin()
    mas_coin.append(a)
for i in range(n):
    j = random.randint(0, 1)
    mas_coin[i].flip(mas_side[j])
    if mas_coin[i].get_side() == "heads":
        counter += 1
print(
    f"За {n} подбрасываний выпало:\nОрлов: {counter}\nРешек: {n-counter}\nПроцент орлов:{counter/n*100}"
)

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
