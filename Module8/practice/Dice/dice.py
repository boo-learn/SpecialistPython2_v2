import random

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.__side = None

    def roll(self):
        self.__side = random.randint(1, self.num_sides)

    # геттер
    @property
    def side(self):
        return self.__side

    # сеттер
    @side.setter
    def side(self, new_value):
        if 1 <= new_value <= self.num_sides:
            self.__side = new_value
        else:
            raise ValueError("Недопустимое значение грани")

    def __lt__(self, other):
        if not isinstance(other, Dice):
            raise TypeError("Невозможно сравнить кубик с другим типом данных")
        if self.__side is None or other.side is None:
            raise ValueError("Сначала нужно подбросить кубики")
        return self.__side < other.side

    def __gt__(self, other):
        if not isinstance(other, Dice):
            raise TypeError("Невозможно сравнить кубик с другим типом данных")
        if self.__side is None or other.side is None:
            raise ValueError("Сначала нужно подбросить кубики")
        return self.__side > other.side

    def __eq__(self, other):
        if not isinstance(other, Dice):
            raise TypeError("Невозможно сравнить кубик с другим типом данных")
        if self.__side is None or other.side is None:
            raise ValueError("Сначала нужно подбросить кубики")
        return self.__side == other.side

num_dice = int(input("Введите количество кубиков: "))
dice_list = []
for i in range(num_dice):
    num_sides = int(input(f"Введите количество граней для кубика {i+1}: "))
    dice = Dice(num_sides)
    dice.roll()
    dice_list.append(dice)

for i, dice in enumerate(dice_list):
    counts = [d.side for d in dice_list].count(dice.side)
    print(f"{dice.side}-ка выпала у {counts} кубиков")

for i in range(num_dice):
    for j in range(i+1, num_dice):
        try:
            if dice_list[i] < dice_list[j]:
                print(f"Кубик {i+1} меньше кубика {j+1}")
            elif dice_list[i] > dice_list[j]:
                print(f"Кубик {i+1} больше кубика {j+1}")
            elif dice_list[i] == dice_list[j]:
                print(f"Кубик {i+1} равен кубику {j+1}")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)


# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте

# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков

# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
