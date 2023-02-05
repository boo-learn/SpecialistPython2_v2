# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
letters = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","э","ю","я"]
slovar_bykv = {"а":0,"б":0,"в":0,"г":0,"д":0,"е":0,"ё":0,"ж":0,"з":0,"и":0,"й":0,"к":0,"л":0,"м":0,"н":0,"о":0,"п":0,"р":0,"с":0,"т":0,"у":0,"ф":0,"х":0,"ц":0,"ч":0,"ш":0,"щ":0,"э":0,"ю":0,"я":0}
slovar = ["Ваасая", "Петя","Ереван", "Катя", "Венера"]

slova_po_bykvam = []
for slovo in slovar:
    slova_po_bykvam.append(slovar_bykv.copy())

numb1 = 0
numb2 = 0

for i,slovo in enumerate(slovar,0):
    for letter in letters:
        slova_po_bykvam[i][letter] = slovar[i].lower().count(letter)
    i += 1

for numb1 in range(len(slova_po_bykvam)):
    for numb2 in range(len(slova_po_bykvam)):
        if (numb1 != numb2) and slova_po_bykvam[numb1] == slova_po_bykvam[numb2] and numb1 > numb2:
            print("Слова " + slovar[numb1] + " и " + slovar[numb2] + " являются анаграммами.")
