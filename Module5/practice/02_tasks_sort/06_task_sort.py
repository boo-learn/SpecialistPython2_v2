sum_goods = [2,1,10,50,10]

sum_goods.sort(reverse = True)

if len(sum_goods) % 2 > 0:
    itog = sum(sum_goods[:len(sum_goods)//2+1])

else:
    itog = sum(sum_goods[:len(sum_goods)//2])

print(sum_goods)

print(itog)
    
