def sort_choise_abs(nums: list) -> None:
    len_nums = len(nums)
    
    for i in range(0, len_nums - 1):
        min_num = i
    
        for j in range(i + 1, len_nums):
            if abs(nums[j]) < abs(nums[min_num]):
                min_num = j
                
        nums[i], nums[min_num] = nums[min_num], nums[i]
        

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
sum_modules = 0

sort_choise_abs(numbers)
print(numbers)
numbers.reverse()

quontity_max_modules = int(input())
print(sum(numbers[:quontity_max_modules]))
