numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10  # Задайте самостоятельно, выбрав произвольное число
fix_numbers = [number for number in numbers if a < number ]
print(sum(fix_numbers))
