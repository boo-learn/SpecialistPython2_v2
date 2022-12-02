from random import randint

class Coin:
    def __init__(self, coin_number: dict):
        self.side = None
        self.coin_number = coin_number

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        new_side = randint(0, 1)
        self.side = new_side

coin_number = [i for i in range(1, int(input("Введите колличество монет: ")) + 1)]
coins = Coin(coin_number)
heads = 0
tails = 0
for i in coin_number:
    coins.flip()
    if coins.side:
        heads += 1
    else:
        tails += 1
print(f'Соотношение орел / решка:{heads} / {tails}')  

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
