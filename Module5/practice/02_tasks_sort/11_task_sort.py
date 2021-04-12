# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).


def bubble_sort(nums, key=lambda x: x, reverse=False):
   swapped = True
   j = 0
   while swapped:
      swapped = False
      for i in range(len(nums) - 1 - j):
         if reverse:
            expr = key(nums[i]) < key(nums[i + 1])
         else:
            expr = key(nums[i]) > key(nums[i + 1])
         if expr:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True
      j += 1
   return nums


def find_anagram(word1: str, word2) -> bool:
    """Принимает две строки и возвращает булево значение в зависимости от того анаграммы слова или нет"""
    word1 = bubble_sort(list(word1.lower()))
    word2 = bubble_sort(list(word2.lower()))
    return word1 == word2


def find_all_anagrams(words: list) -> list:
    """Получает список слов и возвращает список словарей с анаграммами"""
    res = []
    for word in words:
        for subword in words[words.index(word)+1:]:
            if find_anagram(word, subword):
                res.append({'word': word, 'anagram': subword})
    return res


if __name__ == '__main__':
    words = [
        'кабан',
        'банка',
        'мышка',
        'камыш',
        'кукла',
        'кулак',
        'каприз',
        'коршун',
        'шнурок',
        'приказ',
    ]
    print(find_all_anagrams(words))
