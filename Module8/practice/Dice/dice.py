import random


class Dice:
    def __init__(self, facet: int):
        self.__side = None  # private
        self.facet = facet

    def roll(self):
        self.__side = random.randint(1, self.facet)

    @property  # геттер
    def side(self):
        return self.__side

    @side.setter  # сеттер
    def side(self, new_value):
        if 1 <= new_value <= 6 and type(new_value) is int:
            self.__side = new_value
        else:
            raise ValueError('Недопустимое значение стороны')

    def __gt__(self, other_dice: 'Dice') -> bool:
        return self.__side > other_dice.__side

    def __lt__(self, other_dice: 'Dice') -> bool:
        return self.__side < other_dice.__side

    def __eq__(self, other_dice: 'Dice') -> bool:
        return self.__side == other_dice.__side


# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте
dice = Dice(6)
dice.side = 2
# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков
n = 10
dices = [Dice(6) for _ in range(n)]
for i, dice in enumerate(dices):
    dice.roll()
    print(f"Для кубик {i+1} выпало значение {dice.side}")

# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError

dice1 = Dice(6)
dice1.roll()
dice2 = Dice(6)
dice2.roll()

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
dice6 = Dice(6)
dice6.roll()
dice20 = Dice(20)
dice20.roll()
