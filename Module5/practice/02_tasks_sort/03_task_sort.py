numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
summa = 0
i = 0
while i < len(numbers) - 1:

    m = i
    j = i + 1
    while j < len(numbers):
        if numbers[j] < numbers[m]:
            m = j
        j += 1
    numbers[i], numbers[m] = numbers[m], numbers[i]
    i += 1

for i in numbers[i-4:]:
    summa += i


print(numbers)
print(summa)
