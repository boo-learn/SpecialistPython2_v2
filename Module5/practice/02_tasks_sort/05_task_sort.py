import random


def bubble_sort(nums):
    coutn = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                coutn += 1
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    print(coutn)


def gen_list(size, at=0, to=100):
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))
    return data


nums = gen_list(20)
bubble_sort(nums)



