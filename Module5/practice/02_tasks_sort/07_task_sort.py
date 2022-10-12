points = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 10,10,10]

prise = set([points[0]])
points.sort(reverse=True)
i = 0
for point in points:
    if len(prise) < 3:
        prise.add(point)
        i+=1
        
print(prise)
print(i)
