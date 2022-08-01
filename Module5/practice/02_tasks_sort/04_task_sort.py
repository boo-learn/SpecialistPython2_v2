def sort_choice(nums, reserved=False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reserved:
                condition = nums[j] > nums[m]
            else:
                condition = nums[j] < nums[m]
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

new_numbers = []

for num in numbers:
    new_numbers.append(abs(num))

sort_choice(new_numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        index = new_numbers.index((numbers[i] * -1))
        new_numbers[index] = numbers[i]

sum_num = 0
for num in new_numbers[-5:]:
    sum_num += num

print(f'Сумма самых максимальных по модулю чисел списка {new_numbers[-5::]}: {round(sum_num, 1)}')
