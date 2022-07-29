from base_sort import sort_choice
numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = abs(numbers[i])

sort_choice(numbers)

print(numbers[-1:-6:-1])

sum_num = sum(numbers[-1:-6:-1])

print(sum_num)
