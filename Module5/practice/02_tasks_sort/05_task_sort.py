# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
def bubble_sort(nums):
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:
                count += 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return (count)

def gen_list(size, at=-100, to=100):
    import random
    list1 = []
    for _ in range(size):
        k = random.randint(at,to)
        list1.append(k)
    return list1
k = gen_list(10)
print(f' количество обменов: {bubble_sort((k))}')
