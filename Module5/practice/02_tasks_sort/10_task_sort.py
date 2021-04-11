# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

def bubble_sort(nums: list, key=lambda x: x, reverse=False):
    swapped = True
    offset = 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - offset):
            # print("i = ", i)
            if reverse:
                exp = key(nums[i]) < key(nums[i + 1])
            else:
                exp = key(nums[i]) > key(nums[i + 1])
            if exp:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации

                swapped = True
        offset += 1


weights = [70, 1, 2, 3, 4, 5, 6, 7]
bubble_sort(weights)
if len(weights) > 1:
    pile_1 = weights[:len(weights) // 2]
    pile_2 = weights[len(weights) // 2:]
    # print(pile_1, pile_2)
    sum_1 = sum(pile_1)
    sum_2 = sum(pile_2)
    # print(sum_2 / sum_1)
    while sum_2 / sum_1 >= 2:
        pile_1.append(pile_2.pop(0))
        sum_1 = sum(pile_1)
        sum_2 = sum(pile_2)
        # print(sum_2 / sum_1)
    # print(pile_1, pile_2)
    if not sum_2 or (sum_2 / sum_1 >= 2):
        print('Разделить по указанному условию нельзя')
    else:
        print('Разделить удалось')
        print(pile_1, sum(pile_1), pile_2, sum(pile_2))
else:
    print('Разделить удалось, камень был один')
