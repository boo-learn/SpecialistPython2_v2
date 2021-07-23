def sum_more(numbers, a):
    i = 0
    sum_ = 0
    for i in numbers:
        if i > a:
            sum_ += i
    return sum_
