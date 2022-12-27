import random


class Dice:
    def __init__(self, side_num=6):
        self.__side = None
        self.__side_num = side_num

    def roll(self):
        self.__side = random.randint(1, self.__side_num)

    @property
    def side(self):
        return self.__side

    @property
    def side_num(self):
        return self.__side_num

    @side.setter
    def side(self, new_side):
        if isinstance(new_side, int):
            if 1 <= new_side <= self.__side_num:
                self.__side = new_side
            else:
                raise ValueError("Некорректное значение")
        else:
            raise TypeError("Некорректный тип значения")

    def __lt__(self, other):
        if self.__side is None or other.__side is None:
            raise TypeError("Кубики должны быть подброшены")
        return self.__side < other.__side

    def __gt__(self, other):
        if self.__side is None or other.__side is None:
            raise TypeError("Кубики должны быть подброшены")
        return self.__side > other.__side

    def __eq__(self, other):
        if self.__side is None or other.__side is None:
            raise TypeError("Кубики должны быть подброшены")
        return self.__side > other.__side





# Найти некорректные значение, которые можно записать в атрибут .side и исправьте
dice = Dice()
try:
    dice.side = 'шесть'
except TypeError as e:
    print(e)


# Cоздать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
# Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков
n = 10
dices = [Dice() for _ in range(n)]
for dice in dices:
    dice.roll()
points = [dice.side for dice in dices]
print(', '.join([f'{point}-ка выпала у {points.count(point)} кубиков' for point in range(1, 7)]))



#   Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
dice1.side = 5
dice2.side = 3
print(dice1 > dice2)
print(dice1 < dice2)
dice1.side = 3
print(dice1 == dice2)
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError
try:
    print(dice1 == dice3)
except TypeError as e:
    print(e)

# Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
dice6 = Dice()
print(dice6.side_num)
dice20 = Dice(20)
print(dice20.side_num)
dice20.side = 15
print(dice20.side)
