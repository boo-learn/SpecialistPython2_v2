import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        if random.randint(0,1) == 0:
            self.side = "heads"  # random: heads/tails

n = 100
coins = [Coin() for i in range(n)]

heads = 0
for coin in coins: 
    coin.flip()
    if coin.side == "heads":
        heads += 1
print(f"Процент выпадения орла - {(heads/n)*100}, процент выпадения решки - {(1 - heads/n)*100}")



# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
