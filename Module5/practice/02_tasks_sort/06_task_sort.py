# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: дано N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

def choice_sort(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] > nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

# products = list(map(int, input().split()))
products = [10, 2, 50, 1, 10]
choice_sort(products)
print(products)

price = sum(products[:(len(products) + 1) // 2])
print(price)

# Пример
# Вход:
# 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
