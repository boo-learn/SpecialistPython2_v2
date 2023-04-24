numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = int(input('enter a number: '))
total = 0
for num in numbers:
    if num > a:
        total += num
print(total)
