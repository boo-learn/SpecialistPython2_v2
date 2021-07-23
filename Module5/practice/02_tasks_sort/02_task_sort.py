def sum_more_less(numbers, a, b):
    i = 0
    sum_ = 0
    for i in numbers:
        if i > a and i < b:
            sum_ += i
    return sum_
