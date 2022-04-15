numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
summa = 0
a = float(input("Введите число:"))  # Задайте самостоятельно, выбрав произвольное число

for i in range(len(numbers)):
    if numbers[i] > a:
        summa += numbers[i]
print(round(summa, 4))
