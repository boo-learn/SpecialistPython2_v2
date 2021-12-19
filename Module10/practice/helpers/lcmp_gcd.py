import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
  
# Наибольший общий делитель(greatest common denominator) gcd
print("gcd")
print(math.gcd(15, 5))
print(math.gcd(12, 14))
print(math.gcd(7, 12))

# Наименьшее общее кратное(least common multiple) lcm
print("lcm")
print(lcm(15, 5))
print(lcm(12, 14))
print(lcm(4, 12))
