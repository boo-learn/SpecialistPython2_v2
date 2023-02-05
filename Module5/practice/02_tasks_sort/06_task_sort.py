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
prices = [randint(1, 50) for _ in range(N)]
cash_receipt = []
sort_choise(prices)
print(prices)

for i in prices:
    if len(prices) > 1:
        cash_receipt.append(prices[-1])
        cash_receipt.append(prices[0])
        prices = prices[1:-1]
    elif len(prices) == 1:
        cash_receipt.append(prices[0])
        prices.clear()
        
print(*cash_receipt)
