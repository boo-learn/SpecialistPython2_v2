import math
def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] > nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1



numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
numbers_n=numbers

for i in range(len(numbers)):
    numbers_n[i]=abs(numbers[i])

rez=0
sort_choice(numbers_n)
for number_n in numbers_n[:5]:
    for number in numbers:
        if abs(number)==number_n:
            rez+=number
print(numbers_n)


print(rez)
