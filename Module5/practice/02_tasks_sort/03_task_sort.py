# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

def bubble_sort(list: list):
    j = 1
    nums = list
    # print("before sort = ", nums)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    # print("after sort = ", nums)
    return nums


numbers = [1,2,3,4,50,50,50,50,50]
bubble_sort(numbers)
summ = sum(numbers[:3:-1])
print(numbers[::-1])
print(summ)

