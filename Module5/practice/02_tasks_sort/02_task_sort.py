numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 2  # Задайте самостоятельно, выбрав произвольное число
b = 10  # Задайте самостоятельно, выбрав произвольное число
fix_numbers = [number for number in numbers if a < number < b]
print(sum(fix_numbers))
