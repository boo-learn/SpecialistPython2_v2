numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

coefficients = []
for i in range(len(numbers)):
    if numbers[i] < 0:
        coefficients.append(-1)
        numbers[i] = abs(numbers[i])
    else:
        coefficients.append(1)

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            coefficients[j], coefficients[j + 1] = coefficients[j + 1], coefficients[j]
summa = 0
for i in range(len(numbers)):
    summa += numbers[i] * coefficients[i]

print(f"сумма 5-ти самых больших элементов по модулю равна: {summa}")
