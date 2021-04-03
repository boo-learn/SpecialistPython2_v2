# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
my_nums = []
for el in nums:
        abs_el = abs(el)
        my_nums.append(abs_el)
bubble_sort(my_nums)
s = 0
for i in my_nums[-10:]:
    s += i
print(s)
