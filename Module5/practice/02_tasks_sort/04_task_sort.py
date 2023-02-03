def sort_choice(nums: list) -> None:
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


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
sort_choice(numbers)
sum_num = 0
quan_num = 0
first = 0
last = 0
while quan_num != 5:
    if abs(numbers[first]) > abs(numbers[len(numbers)-1-last]):
        sum_num += numbers[first]
        first += 1
        quan_num += 1
    else:
        sum_num += numbers[len(numbers)-1-last]
        last += 1
        quan_num += 1

print(sum_num)
