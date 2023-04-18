import random


class Coin:
    def __init__(self):
        self.side = None


    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.randint(0, 1) # Пусть 1 будет орёл, 0 решка


lst_coins = []
numb = input("Введите количество монет ")
for i in range(int(numb)):
    up = Coin()
    up.flip()
    lst_coins.append(up.side)
ratio = round((lst_coins.count(1)*100)/len(lst_coins), 2)

print(f"Орлов {ratio}%, решек {100-ratio}%")
