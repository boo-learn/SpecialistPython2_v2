def reduce_loss(n, values):
    values.sort()
    half_index = -n//2
    return sum(values[half_index:])


print(reduce_loss(6, [5, 2, 1, 10, 50, 10]))
