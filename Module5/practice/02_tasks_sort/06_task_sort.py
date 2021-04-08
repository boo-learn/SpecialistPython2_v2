def bubble_sort(nums, key=lambda x: x, reverse=False):
    j = 0
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - j - 1):
            # print("i = ", i)
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    return nums

a = 4
p = 0
gen = [1, 3, 4, 3, 5, 6, 7, 7, 6, 1]
print('before: ', gen)
bubble_sort(gen)
print('sort: ', gen)

for i in gen:
    if i > a:
        p += 1

print('prizea: ', p)
