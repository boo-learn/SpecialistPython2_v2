def parse_fraction(raw_fraction: str):
    """
    Извлекает из строки элементы дроби: целую часть(whole), числитель(numerator) и знаменатель(denominator).
    Также определяет знак дроби(sign) +/-
    """
    sign = 1
    if raw_fraction.startswith("-"):
        sign = -1
        raw_fraction = raw_fraction[1:]
    pair = raw_fraction.split()
    whole = 0
    if len(pair) == 2:
        whole = int(pair[0])
        raw_fraction = pair[-1]
    pair = raw_fraction.split('/')
    numerator = int(pair[0])
    denominator = int(pair[1])
    return {"sign": sign, "whole": whole, "numerator": numerator, "denominator": denominator}


print(parse_fraction("-2 4/5"))
print(parse_fraction("-7/8"))
print(parse_fraction("3/8"))
print(parse_fraction("7 3/8"))