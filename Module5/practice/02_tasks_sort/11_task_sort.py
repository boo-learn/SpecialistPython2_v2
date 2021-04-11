# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
def bubble_sort(nums: list, key=lambda x: x, reverse=False):
    swapped = True
    offset = 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - offset):
            # print("i = ", i)
            if reverse:
                exp = key(nums[i]) < key(nums[i + 1])
            else:
                exp = key(nums[i]) > key(nums[i + 1])
            if exp:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации

                swapped = True
        offset += 1


words = ['дома', 'насос', 'куб', 'Рим', 'сосна', 'мода', 'тело', 'мир', 'лето']

dict_word = dict.fromkeys(words)

for word in words:
    sorted_word = list(word.lower())
    bubble_sort(sorted_word)
    dict_word[word] = ''.join(sorted_word)
printed_values = []
for k, v in dict_word.items():
    for k1, v1 in dict_word.items():
        if v == v1 and k != k1 and v not in printed_values:
            print(f'Анаграмма найдена! {k} -> {k1}')
            printed_values.append(v1)
if not printed_values:
    print('Анаграмм не обнаружено.')
