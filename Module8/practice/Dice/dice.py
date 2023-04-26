import random


class Dice:
    def __init__(self, sides_quantity: int = 6):
        self.__side = None
        self.__sides_quantity = sides_quantity

    @property
    def side(self) -> int:
        return self.__side

    @side.setter
    def side(self, new_side: int):
        if 1 <= new_side < self.__sides_quantity:
            self.__side = new_side
        else:
            raise ValueError("Некорректное значение!")

    def roll(self):
        self.__side = random.randint(1, self.__sides_quantity)

    def both_rolled(self, other_dice) -> bool:
        if self.side and other_dice.side:
            return True
        else:
            raise TypeError("Необходимо подбросить оба кубика!")

    def __lt__(self, other_dice) -> bool:
        if self.both_rolled(other_dice):
            return self.side < other_dice.side

    def __gt__(self, other_dice) -> bool:
        if self.both_rolled(other_dice):
            return self.side > other_dice.side

    def __eq__(self, other_dice) -> bool:
        if self.both_rolled(other_dice):
            return self.side == other_dice.side

# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков


SIDES_DICE_6 = ["1-ца", "2-ка", "3-ка", "4-ка", "5-ка", "6-ка"]

n = 10

dices = []
sides_counter = [0] * 6

i = 0
while i < n:
    dices.append(Dice())
    dices[i].roll()
    sides_counter[dices[i].side - 1] += 1
    i += 1

print("TODO-2")
# for dice in dices:
#     print(dice.side, end="; ")
# print()
# for side in sides_counter:
#     print(side, end="; ")
# print()

temp_str = ""
for i, sides in enumerate(sides_counter):
    str_end = "а" if sides_counter[i] == 1 else "ов"
    temp_str += f"{SIDES_DICE_6[i]} выпала у {sides_counter[i]} кубик{str_end}, "
print(temp_str[:-2])

# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError

dice1 = Dice()
dice1.roll()
dice2 = Dice()
dice2.roll()

print("TODO-3")
# print(f"Первый кубик: {dice1.side} ; второй кубик: {dice2.side}")

if dice1 > dice2:
    print(f"Сторона {SIDES_DICE_6[dice1.side - 1]} больше, чем сторона {SIDES_DICE_6[dice2.side - 1]}")
elif dice1 < dice2:
    print(f"Сторона {SIDES_DICE_6[dice1.side - 1]} меньше, чем сторона {SIDES_DICE_6[dice2.side - 1]}")
else:
    print(f"Сторона {SIDES_DICE_6[dice1.side - 1]} равна стороне {SIDES_DICE_6[dice2.side - 1]}")

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик

print("TODO-3")
dice6 = Dice(6)
dice6.roll()
dice20 = Dice(20)
dice20.roll()
print(f"Сторона первого кубика: {dice6.side} ; сторона второго кубика: {dice20.side}")
