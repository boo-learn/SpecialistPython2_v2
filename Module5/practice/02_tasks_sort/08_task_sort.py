phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

def sort_phones(baza):
    i = 0
    while i < len(baza) - 1:
        m = i
        j = i + 1
        while j < len(baza):
            if baza[j] < baza[m]:
                m = j
            j += 1
        baza[i], baza[m] = baza[m], baza[i]
        i += 1
    return baza
    
print(sort_phones(phones))
