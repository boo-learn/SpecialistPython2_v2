def summa(list, A):
    sum=0
    for i in list:
        if i>A:
            sum+=i
    return sum

summa ([4,5,7,3,2,10],5)
