from random import randint

def sort_choise(nums: list) -> None:
    len_nums = len(nums)
    
    for i in range(0, len_nums - 1):
        min_num = i
    
        for j in range(i + 1, len_nums):
            if nums[j] < nums[min_num]:
                min_num = j
                
        nums[i], nums[min_num] = nums[min_num], nums[i]
        
N = int(input())

results = [randint(1, 10) for _ in range(N)]
sort_choise(results)
bronze = list(set(results))[-3] 
number_of_winners = sum([1 for i in results if i >= bronze])

print(bronze)
print(results)
print(number_of_winners)
