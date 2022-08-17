def sort_choice(nums):
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

numbers = [10, 2, 50, 1, 10]
sort_choice(numbers)
print(numbers)
numbers.reverse()
if len(numbers) / 2 == 0:
    print(sum(numbers[:int(len(numbers) / 2 + 1)]))
else:
    print('Result: ', sum(numbers[:int(len(numbers) / 2 + 0.5)]))
