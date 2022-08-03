# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

ef split_stones(stones):
    stones.sort(reverse=True)
    mark = sum(stones[1:]) * 2
    if stones[0] >= mark:
        return [], []
    else:
        pile1, pile2 = [], []
        for _ in stones:
            pile1.append(stones.pop(0))
            pile2.append(stones.pop(0))
            while sum(pile1) >= sum(pile2) * 2:
                pile2.append(stones.pop(0))
            if len(stones) == 1:
                pile2.append(stones.pop(0))
        return pile1, pile2


if __name__ == "__main__":
    stones = [5, 9, 10, 13, 14, 16, 100]
    pile1, pile2 = split_stones(stones)
    if len(pile1) != 0 and len(pile2) != 0:
        print("Куча 1:", pile1)
        print("Куча 2:", pile2)
    else:
        print("Разделение на две кучи так, чтобы одна была не больше чем в два раза больше другой, невозможно")
