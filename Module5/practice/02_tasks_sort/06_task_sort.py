# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход:дано N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10

def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if i % 2 == 0:
                if nums[j] > nums[m]:
                    m = j
            else:
                if nums[j] < nums[m]:
                    m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


numbers = []

cheque = input("Введите цены товаров: ")
numbers = cheque.split(" ")

numbers = [int(_) for _ in numbers]

sort_choice(numbers)

sum_price = 0

for i in range(len(numbers)):
    if i % 2 == 0:
        sum_price = sum_price + numbers[i]
print(sum_price)

