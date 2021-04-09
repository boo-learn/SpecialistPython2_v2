# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).


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


words = ['qwertyuiop', 'twoplussix', 'poiuytrewq', 'plustwosix', 'poiuqwerty']


anagramms = {}
for w in words:
    ls = list(w)
    ls_sort = bubble_sort(ls)
    ls = "".join(ls_sort)
    anagramms.setdefault(ls, [])
    anagramms[ls].append(w)

for a in anagramms.values():
    print(*a)
