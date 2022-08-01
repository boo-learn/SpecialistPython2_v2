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
point = [1, 3, 4, 3, 5, 6, 7, 7, 6, 1, 6, 10,7,7,7,7,7,10,10,10,10,10]


def sort_choice(nums, reverse=True, key=lambda n: n):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1

        while j < len(nums):
            if reverse:
                condition = key(nums[j]) > key(nums[m])
            else:
                condition = key(nums[j]) < key(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


sort_choice(point)
print(point)
count = 0
index = 0
winners = 0
while count < 3:
    if point[index] > point[1 + index]:
        count += 1
        index += 1
        winners += 1
    else:
        index += 1
        winners += 1
print(winners)
