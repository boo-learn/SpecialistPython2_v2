# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

def bubble_sort(nums, key=lambda x: x, reverse=False):
    j = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j - 1):
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    return nums


def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов вдиапазоне at..to 
    """
    random_list = [random.randint(at, to) for i in range(size)]
    return random_list


n = 10
points = gen_list(n, at=1, to=10)
print(n, points)
points_sort = bubble_sort(points, reverse=True)
print(points_sort)
prev_point = points_sort[0]
steps = 0
num_people = 0
for point in points_sort:
    if point < prev_point:
        steps += 1
        prev_point = point
    if steps > 2:
        break
    num_people += 1
print(num_people)
