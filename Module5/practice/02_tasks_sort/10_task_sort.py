# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.


def bubble_sort(nums, key=lambda x: x, reverse=False):
   swapped = True
   j = 0
   while swapped:
      swapped = False
      for i in range(len(nums) - 1 - j):
         if reverse:
            expr = key(nums[i]) < key(nums[i + 1])
         else:
            expr = key(nums[i]) > key(nums[i + 1])
         if expr:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True
      j += 1
   return nums


def get_two_heaps(rocks):
    """Получает кучу камней разной массы и старается разбить на одинаковые кучки"""
    rocks = bubble_sort(rocks)
    heap1 = []
    heap2 = []
    for i in range(len(rocks) // 2):
        if i % 2 == 0:
            heap1.append(rocks[i])
            heap1.append((rocks[len(rocks) - i - 1]))
        else:
            heap2.append(rocks[i])
            heap2.append((rocks[len(rocks) - i - 1]))
    if len(rocks) % 2 != 0:
        heap2.append(rocks[len(rocks) // 2])
    heap1 = bubble_sort(heap1, reverse=True)
    heap2 = bubble_sort(heap2, reverse=True)
    difference = sum(heap1) / sum(heap2)
    while difference >= 2:
        if heap1[0] > (sum(heap1[1:]) + sum(heap2)):
            return False, False
        half_substr_diff = (sum(heap1) - sum(heap2)) / 2
        for h1 in heap1:
            if h1 <= half_substr_diff:
                heap2.append(h1)
                heap1.remove(h1)
                break
        difference = sum(heap1) / sum(heap2)
    return heap1, heap2


if __name__ == '__main__':
    rocks = [1, 50, 36, 7, 25, 70, 4, 86, 5, 9, 34, 34, 7, 2, 61, 52, 76]
    print(rocks)
    heap1, heap2 = get_two_heaps(rocks)
    if not heap1 and not heap2:
        print('Нельзя составить две кучки')
    else:
        print(f'{heap1=}')
        print(f'{heap2=}')
        print(f'len rocks {len(rocks)} heap1 {len(heap1)} heap2 {len(heap2)}')
        print(f'sum heap1 {sum(heap1)} heap2 {sum(heap2)}')
