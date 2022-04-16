import random


# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.
def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1


incoming_list = []
N = random.randint(2, 1000)
for i in range(N):
    incoming_list.append(random.randint(1, 50))

bubble_sort(incoming_list)

list_of_free = []
list_to_pay = []

list_of_free = incoming_list[:len(incoming_list) // 2]
list_to_pay = incoming_list[len(incoming_list) // 2:]

itogo = []
for i in range(len(list_to_pay)):
    itogo.append(list_to_pay[i])
    if len(list_of_free) > i:
        itogo.append(list_of_free[i])
print(f"максимальная сумма в чеке: {sum(list_to_pay)} \n"
      f"Последовательность для пробития товаров: {itogo}")
# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
