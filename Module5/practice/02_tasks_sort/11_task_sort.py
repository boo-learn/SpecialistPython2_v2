# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

def choice_sort(nums, reverse = False, key = lambda n: n):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                condition = key(nums[j]) > key(nums[m])
            else:
                condition = key(nums[j]) < key(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

def convertation(word):
    return list(word)

words = ['нос', 'сосна', 'жилы', 'сон', 'банка', 'лыжи', 'парк', 'насос', 'карп', 'сон', 'кабан', 'баклан']
words_sorted = words[:]


for i in range(len(words_sorted)):
    words_sorted[i] = list(words_sorted[i])
    choice_sort(words_sorted[i])


index_found = set()
words_found = []
for _ in words:
    words_found.append([])

for i in range(len(words_sorted) - 1):
    for j in range(i + 1, len(words_sorted)):
        if words_sorted[i] == words_sorted[j] and i not in index_found:
            if words[i] not in words_found[i]:
                words_found[i].append(words[i])
            words_found[i].append(words[j])
            index_found.add(j)

for word in words_found:
    if word:
        print(*word)
