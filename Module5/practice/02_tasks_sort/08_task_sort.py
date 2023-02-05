def sort_choise(nums: list) -> None:
    len_nums = len(nums)
    
    for i in range(0, len_nums - 1):
        min_num = i
    
        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_num]:
                min_num = j
                
        nums[i], nums[min_num] = nums[min_num], nums[i]

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
sort_choise(phones)
print(phones)
