def bubble_sort(nums, key=lambda x: x, reverse=False):
    j = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j - 1):
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums

n = 9
price = [2, 45, 13, 67, 1, 88, 16, 55, 9]
bubble_sort(price, reverse = True)
m = int(n/2)
s = sum(price[:m + 1])
print(s)
