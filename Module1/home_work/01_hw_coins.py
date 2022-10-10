import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        choices = ['heads', 'tails']
        self.side = random.choices(choices)  # random: heads/tails


if __name__ == '__main__':
    val = int(input('Введите количество монет : '))
    counter = 0
    coin_list = [Coin() for _ in range(val)]
    for i in coin_list:
        i.flip()
        if i.side == ['heads']:
            counter += 1
    print(f'Процент орлов : {int(counter/val * 100)}')
    print(f'Процент решек : {int((val-counter)/val * 100)}')


# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
