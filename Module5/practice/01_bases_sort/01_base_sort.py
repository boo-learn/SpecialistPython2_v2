nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
shorter = 0
while swapped:
    swapped = False
    print("*****")
    shorter += 1
    for i in range(len(nums) - shorter):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)
