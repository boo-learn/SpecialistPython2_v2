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
def sort_choice(nums, key=lambda el: el, reverse=False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            compare = key(nums[j]) > key(nums[m]) if reverse else key(nums[j]) < key(nums[m])
            if compare:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


recipe = [5, 2, 1, 10, 50, 10]
sort_choice(recipe)
print(sum(recipe[-len(recipe)//2:]))
