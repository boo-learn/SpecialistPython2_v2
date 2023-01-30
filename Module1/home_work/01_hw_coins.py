import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        coin_choise = ["heads", "tails"]
        self.side = random.choice(coin_choise)  # random: heads/tails


def percentage(part, all):
    perc = 100 * part/all
    return str(perc) + "%"



while True:
    coins = input('Введите количество монеток:')
    try:
        coins = int(coins)
        coins_list = [Coin()] * coins
        tail_count = 0
        head_count = 0

        for coin in coins_list:
            coin.flip()
            if coin.side == "heads":
                head_count += 1
            else:
                tail_count += 1


        print("Процент орлов:", percentage(head_count, coins))
        print("Процент решек:",percentage(tail_count, coins))
        break
        
    except:
        print("Введено не число! Попробуйте еще раз.")

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
