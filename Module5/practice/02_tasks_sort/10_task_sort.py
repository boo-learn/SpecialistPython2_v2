# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
import random


def break_in_two_piles(sl):
    p1 = []
    p2 = []
    s = sum(sl)
    max_weight = (2 * s) / 3
    sl.sort(reverse=True)
    for s in sl:
        if sum(p1) + s > max_weight:
            if sl.index(s) == 0:
                return None
            else:
                p2.append(s)
        else:
            p1.append(s)
    return p1, p2


N = 10
stone_list = [random.randint(1, 10) for _ in range(N)]
#stone_list = [10, 1, 1] # will not split this
print(stone_list)
piles = break_in_two_piles(stone_list)
if piles is None:
    print("Cannot split in such piles.")
else:
    p1, p2 = piles[0], piles[1]
    print(p1, p2)
    print(f"Sum of pile 1 is {sum(p1)}")
    print(f"Sum of pile 2 is {sum(p2)}")
    print(f"Wp1 / Wp2 is {sum(p1)/sum(p2)}")
