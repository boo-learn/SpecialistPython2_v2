import random

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]

# Для проверки: a = 0, b = 10, sum_a_b = 7 (3 + 4)
a = random.uniform(min(numbers), max(numbers))
b = random.uniform(a, max(numbers))

sum_a_b = sum([item for item in numbers if a < item < b ])

print(f'a = {a}  b = {b}')
print(f'{sum_a_b}')
