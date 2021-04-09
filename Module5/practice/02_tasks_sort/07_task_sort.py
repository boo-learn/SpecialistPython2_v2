# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10

def bubble_sort(nums, key=lambda x: x, reverse=False):
    count = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                count += 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    # print(f'{count=}')


def gen_list(size, at=-100, to=100):
    import random
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


purchases = gen_list(22, 0, 100)
print(*purchases)
bubble_sort(purchases)
print(*purchases)
print(sum(purchases[int(len(purchases) / 2):]))
