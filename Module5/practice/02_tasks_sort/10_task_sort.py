# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.


def heap_stones(n, *stones) -> tuple or None:
    """"
    Разбить камни на две кучи таким образом, 
    чтобы веса куч отличались не более чем в 2 раза.
    :param n: количество камней
    :param stones: веса камней
    :return: две кучи камней или None
    """
    stones = list(stones)
    if n != len(stones):
        raise ValueError('Число камней должно быть равно {n}')
    stones.sort()
    one, two = [], []
    for stone in stones:
        if sum(one) < sum(two):
            one.append(stone)
        else:
            two.append(stone)
    if  0.5 <=  sum(one) / sum(two) <= 2:
        return one, two
    else:
        print('Деление невозможно')
        return


a = heap_stones(10, 34, 235, 234, 56, 34, 34, 65, 34, 8, 90)
print(a)
