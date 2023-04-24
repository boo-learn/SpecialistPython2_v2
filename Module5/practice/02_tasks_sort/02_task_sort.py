numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = int(input('enter a number a: '))  # Задайте самостоятельно, выбрав произвольное число
b = int(input('enter a number b: '))  # Задайте самостоятельно, выбрав произвольное число
total = 0
for num in numbers:
    if a < num < b:
        total += num
print(total)
