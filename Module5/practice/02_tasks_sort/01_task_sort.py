import random

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]

# Для проверки: a = 0, b = 10, sum_more_a = 73.6
a = random.uniform(min(numbers), max(numbers))
print(a)

sum_more_a = sum([item for item in numbers if item > a])
print(f'{sum_more_a}')
