def choice_sort(nums, reverse = False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                condition = nums[j] > nums[m]
            else:
                condition = nums[j] < nums[m]
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


# n = int(input("Введите число участников: "))
# results = list(map(int, input("Введите результаты участников через пробел: ").split()))
results = [10, 1, 3, 4, 5, 6, 7, 7, 6, 1]
choice_sort(results, 1)
print(results)
winner_count = 0

winners_results = set()
for result in results:
    if result not in winners_results:
        winners_results.add(result)
    if len(winners_results) > 3:
        break
    winner_count += 1

print(winner_count)


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
