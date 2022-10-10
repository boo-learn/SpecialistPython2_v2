import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(['heads','tails'])

n = int(input("Введите число: "))
print(n)
coinlist = []

for i in range(0, n): # создание списка монет
    coin = Coin()
    coinlist.append(coin)

for i in range(0, n): # подбрасывание каждой монеты
    coinlist[i].flip()
    print(coinlist[i].side)
h = 0
t = 0
for coin_i in coinlist:
    if coin_i.side == "heads":
        h += 1
    else:
        t += 1

print("Tails = ", t/n*100, "%")
print("Heads = ", h/n*100, "%")
# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
