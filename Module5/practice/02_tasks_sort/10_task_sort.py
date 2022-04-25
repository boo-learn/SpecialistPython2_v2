import itertools
import random


def checking(input_data, i):
    minimum = abs(sum(input_data[:0]) - sum(input_data[0:]))
    minimum_position = 0
    for number in range(len(input_data)):
        if abs(sum(input_data[:number]) - sum(input_data[number:])) < minimum:
            minimum = abs(sum(input_data[:number]) - sum(input_data[number:]))
            minimum_position = number
    return [i, minimum_position, minimum]


stones = []
result_list = []
reshenie = []
value = True
counter = 0

for i in range(random.randint(3, 10)):
    stones.append(random.randint(1, 50))

# stones = [6,1,4]

print(stones)
perebor = itertools.permutations(stones)

for i in perebor:
    result_list.append(list(i))
    reshenie.append(checking(result_list[-1], counter))
    if reshenie[-1][-1] == 0:
        print("Камни можно разделить поровну")
        print(
            f"Кучка номер 1 {(result_list[-1][(reshenie[-1][-2]):])} сумма равна {sum(result_list[-1][(reshenie[-1][-2]):])}")
        print(
            f"Кучка номер 2 {(result_list[-1][:(reshenie[-1][-2])])} сумма равна {sum(result_list[-1][:(reshenie[-1][-2])])}")
        value = False
        break
    counter += 1

if value:
    reshenie.sort(key=lambda x: x[-1])
    if 0.5 < sum(result_list[reshenie[0][0]][(reshenie[0][-2]):]) / sum(
            result_list[reshenie[0][0]][:(reshenie[0][-2])]) < 2:
        print("Самое близкое к равному деление соответствует кучкам")
        print(
            f"Кучка номер 1 {(result_list[reshenie[0][0]][(reshenie[0][-2]):])} сумма равна {sum(result_list[reshenie[0][0]][(reshenie[0][-2]):])}")
        print(
            f"Кучка номер 2 {(result_list[reshenie[0][0]][:(reshenie[0][-2])])} сумма равна {sum(result_list[reshenie[0][0]][:(reshenie[0][-2])])}")
    else:
        print("Данную кучу камней невозможно разделить так, чтобы кучки удовлетворяли условиям задачи")
