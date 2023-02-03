numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 2  # Задайте самостоятельно, выбрав произвольное число

num_sum = 0
for num in numbers:
    if num > a:
        num_sum += num

print(num_sum)
