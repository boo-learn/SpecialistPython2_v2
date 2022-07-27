def bubble_sort(nums):
    swapped = True
    k = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - k):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        k += 1
    return nums

sum1 = 0
numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
res = bubble_sort(numbers)[::-1]
for i in range(5):
    sum1 += res[i]

print(sum1)

