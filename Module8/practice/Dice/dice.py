import random


class Dice:
    def __init__(self):
        self.__side = None

    @property
    def side(self):  # геттер
        return self.__side

    @side.setter
    def side(self, new_value):  # сеттер
        if 1 <= new_value <= 6:
            self.__side = int(new_value) 
        else:
            raise ValueError("Только число [1, 6]")

    def roll(self):
        self.__side = random.randint(1, 6)


# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте
'''дробное число'''
dice = Dice()

dice.side = 1.3


# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков

def generate_dices(num: int) -> list:
    dices = []
    for i in range(int(num)):
        dice_i = f"dice_{i}"
        dice_i = Dice()
        dices.append(dice_i)
    return dices

dices = generate_dices(8)

sides = []
for dice in dices:
    dice.roll()
    sides.append(dice.side)
print(sides)

for i in range(1, 7):
    if sides.count(i) != 0:
        print(f"{i}-ка выпала у кубика {sides.count(i)}")


# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
