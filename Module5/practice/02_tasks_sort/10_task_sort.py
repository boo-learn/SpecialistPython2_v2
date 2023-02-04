import random as r


def sort_choice(nums: list) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


n = 10
stones = [r.randint(1, 100) for _ in range(n)]
mountains = {"small": [], "big": []}

sort_choice(stones)
print(stones,"\n")

mountains["big"].append(stones.pop(-1))

while True:
    small = sum(mountains["small"])
    others = sum(stones)
    big = sum(mountains["big"])
    if small < big:
        if 0.5 < big/(others + small) < 2:
            mountains["small"] += stones
            break
        elif big/(others + small) >= 2:
            print("It's UNREAL!")
            mountains["small"] += stones
            break
        else:
            try:
                mountains["small"].append(stones.pop(-1))
            except IndexError:
                mountains["small"] += stones
            if 0.5 < (others + small)/big < 2:
                mountains["small"] += stones
                break
    else:
        try:
            mountains["big"].append(stones.pop(0))
        except IndexError:
            mountains["big"] += stones
            break

print(mountains,"\n")
print(f" small / big = {sum(mountains['big'])/sum(mountains['small'])}")
# получилось не очень красиво но работает)
