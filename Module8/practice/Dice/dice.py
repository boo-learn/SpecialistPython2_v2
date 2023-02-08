import random


class Dice:
    def __init__(self, sides_number = 6):
        self.__side = None  # private
        self.sides_number = sides_number

    def roll(self):
        self.__side = random.randint(1, self.sides_number)

    @property  # геттер
    def side(self):
        return self.__side

    @side.setter  # сеттер
    def side(self, new_value):
        if 1 <= new_value <= self.sides_number:
            self.__side = new_value
        else:
            raise ValueError('Недопустимое значение стороны')




# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте
dice1 = Dice(6)
dice1.roll()
dice1.side = 5

# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков
N = 3
dices = []
side_numbers = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

for i in range(N):
    dice = Dice(6)
    dices.append(dice)

for dice in dices:
    dice.roll()
    side_numbers[str(dice.side)] = side_numbers[str(dice.side)] + 1

for side, value in side_numbers.items():
    print(f" Сторона {side} выпала {value} раз")


# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError
def compare(dice1,dice2):
    if dice1.side > dice2.side:
        print(f"Сторона кубика 1 больше стороны кубика 2")
    elif dice1.side < dice2.side:
        print(f"Сторона кубика 2 больше стороны кубика 1")
    elif dice1.side == dice2.side:
        print(f"Стороны кубиков равны.")
    else:
        print(f"Один или более кубиков не подброшены.")
compare(dices[1],dices[2])

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
dice20 = Dice(20)
