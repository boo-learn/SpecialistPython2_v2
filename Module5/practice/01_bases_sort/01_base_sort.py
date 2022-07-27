nums = [5, 2, 1, 8, 4, 9, 10, 2]
print("before sort = ", nums)
swapped = True
for j in range(len(nums)):
    swapped = False
    # print("*****")
    for i in range(len(nums) - 1 - j):
        # print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    if not swapped:
        break
print("after sort = ", nums)
