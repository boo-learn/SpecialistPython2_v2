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


def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]


def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums


def rewarding(people: list):
    people = bubble_sort(people, reverse=True)
    prev = people[0]
    prizes = 0
    steps = 1
    for human in people:
        if steps <= 3:
            prizes += 1
            if prev != human:
                steps += 1
        prev = human
    return prizes - 1

if __name__ == '__main__':
    olympigs = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1]
    winners = rewarding(olympigs)
    print(f'Призёров всего : {winners}')
