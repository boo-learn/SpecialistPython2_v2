import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        luck = ['heads', 'tails']
        random.shuffle(luck)
        self.side = luck[0]  # random: heads/tails
        

# Сколько хотим монет?
num_of_coins = 15
i = 0
coins = []
while i < num_of_coins:
    coins.append(Coin())
    i += 1

# количество орлов и решек перед перемешиванием
head = 0
tail = 0

for monetka in coins:
    monetka.flip()
    if monetka.side == 'heads':
        head += 1
    else:
        tail += 1
head_perc = head / (head + tail) * 100
tail_perc = tail / (head + tail) * 100
print(f"Орлы выпали в {head_perc}% случаев ({head} орлов) \nРешки выпали в {tail_perc}% случаев ({tail} решек)")



# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
