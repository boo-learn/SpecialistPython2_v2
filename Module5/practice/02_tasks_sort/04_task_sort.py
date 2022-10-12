def sort_choice(nums, revers=False): # True/False
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if revers:
                condition = abs(nums[j]) > abs(nums[m])
            else:
                condition = abs(nums[j]) < abs(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
sort_choice(numbers, True)
numbers_sum = 0
for i in range(5):
    numbers_sum += numbers[i]

print(numbers)
print(numbers_sum)
