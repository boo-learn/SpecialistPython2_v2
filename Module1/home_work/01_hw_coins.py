import random

class Coin:
    def __init__(self):
        # heads-орел 0 /tails-решка 1
        self.side = None

    def flip(self):

        # Подбрасывание монетки
        #sidevar = [0, 1]
        #self.side = random.choices(sidevar)[-1]
        self.side = random.randint(0, 1)
         # random: heads/tails

    def show(self):
        return f"{self.side}"

coin1 = Coin()
coin2 = Coin()
coin3 = Coin()
coin4 = Coin()
coin5 = Coin()

allcoins = [coin1, coin2, coin3, coin4, coin5]
coin1.flip()
print(coin1.show())
head = 0
tail = 0
for coin in allcoins:
    coin.flip()
    if coin.side == 0:
        print("орел")
        head += 1
    else:
        print("решка")
        tail += 1

print("соотношение в процентах орлов ко всем монетам", (head / (head + tail)) * 100)
print("соотношение в процентах решек ко всем монетам", (tail / (head + tail)) * 100)
print("соотношение в процентах орлов к решкам", (head / tail) * 100)


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
