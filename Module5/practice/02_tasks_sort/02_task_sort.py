
numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 5 # Задайте самостоятельно, выбрав произвольное число
b = 20  # Задайте самостоятельно, выбрав произвольное число
sum_numbers = 0
for number in numbers:
    if number > a and number < b:
        sum_numbers += number

print(sum_numbers)
