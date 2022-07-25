import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    # Подбрасывание монетки
    def flip(self):
        self.side = random.randint(0, 1)  # random: 0=heads, 1=tails


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
coin_qnt = -1
while 1 > coin_qnt or coin_qnt > 10000:
    coin_qnt = int(input("Задайте число монет [1-10000]: "))
    print(coin_qnt)

stack_of_coins = [None] * coin_qnt

heads = 0
tails = 0
coin_toss = Coin()

for coin in range(0, coin_qnt):
    coin_toss.flip()
    stack_of_coins.append(coin_toss)
    if coin_toss.side == 0:
        heads += 1
    elif coin_toss.side == 1:
        tails += 1

print(f'Вероятность выпадения орла {heads/(heads+tails)}')

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
