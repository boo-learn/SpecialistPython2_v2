def sort_choise(nums: list) -> None:
    len_nums = len(nums)
    
    for i in range(0, len_nums - 1):
        min_num = i
    
        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_num]:
                min_num = j
                
        nums[i], nums[min_num] = nums[min_num], nums[i]

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

quontity_max_numbers = int(input())
sort_choise(numbers)
numbers.reverse()

print(numbers)
print(sum(numbers[:quontity_max_numbers]))

