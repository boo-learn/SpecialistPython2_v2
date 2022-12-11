numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]


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
    

abs_numbers = [abs(number) for number in numbers]
sort_choice(abs_numbers)
abs_numbers[-5 : len(abs_numbers)]
out_numbers = []
for abs_number in abs_numbers[-5 : len(abs_numbers)]:
    for number in numbers:
        if abs_number == abs(number) and number not in out_numbers:
            out_numbers.append(number)

print(sum(out_numbers))
            
