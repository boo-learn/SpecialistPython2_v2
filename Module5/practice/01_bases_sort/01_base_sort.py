nums = [5, 2, 1, 8, 4]
j = 0
print("before sort = ", nums)
swapped = True
while swapped:
    swapped = False
    print("*****")
    j += 1
    for i in range(len(nums) - j):
        print("i = ", i)

        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)


