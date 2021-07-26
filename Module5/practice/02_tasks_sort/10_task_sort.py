# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
stones = [10, 7, 8, 12, 1, 3, 5, 1, 3, 16, 17, 10, 7]


def stones_divider(stones):
    heap1 = []
    heap2 = []
    for i in stones:
        if sum(heap1) <= sum(heap2):
            heap1.append(i)
        elif sum(heap1) > sum(heap2):
            heap2.append(i)
    if 0.5 <= sum(heap1) / sum(heap2) <= 2:
        return heap1, heap2
    else:
        return "Невозможно разделить на две кучи"

print(stones_divider(stones))
