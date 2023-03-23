import random


class Dice:
    def __init__(self):
        self.__side = None
        self.__rolled = 0

    @property
    def side(self):  # геттер
        return self.__side

    @side.setter
    def side(self, new_value):  # сеттер
        if type(new_value) == int: # т.к можно было ввести float, или упасть с ошибкой на условии сравнения при char
            if 1 <= new_value <= 6:
                self.__side = new_value
            else:
                raise ValueError("Только целое число [1, 6]")
        else: 
            raise ValueError("Только целое число [1, 6]")

    def roll(self):
        self.__side = random.randint(1, 6)
        self.__rolled = 1
        
    def compare(self, other_dice):
        if self.__rolled == 1 and other_dice.__rolled == 1:
            if self.__side > other_dice.__side:
                print(f"Кубик {self.__side} больше кубика {other_dice.__side}")
            elif self.__side < other_dice.__side:
                print(f"Кубик {self.__side} меньше кубика {other_dice.__side}")
            else: 
                print("Кубики равны")
        else:
            raise TypeError("Оба кубика должны быть предварительно подброшены")
        
# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте  +
dice1 = Dice()
dice2 = Dice()
dice1.roll()
dice2.roll()
print(dice1.side, ' ', dice2.side)

# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков
   


# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError
dice1.compare(dice2)
dice2.compare(dice1)
# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
