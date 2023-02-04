import random as r


def sort_choice(nums: list) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


n = 10
# создаем список из случайных чисел от 1 до 15 в количестве n
cost_list = [r.randint(1, 15)for _ in range(n)]
# сортируем список цен
sort_choice(cost_list)
# инвертируем что бы самые дорогие товары были первыми
cost_list = cost_list[-1::-1]
# список в который будем записывать результат
res_list = []
if n % 2 != 0:  # если товаров не четное количество то действеум
    res_list.append(cost_list[0])
    cost_list = cost_list[1:]
    for i in range(len(cost_list)//2):
        res_list.append(cost_list[-1-i])
        res_list.append(cost_list[i])
else:  # если товаров четное количество
    for i in range(len(cost_list)//2):
        res_list.append(cost_list[i])
        res_list.append(cost_list[-1-i])

print(res_list)
