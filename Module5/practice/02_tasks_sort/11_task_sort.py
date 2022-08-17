anagrams = {1: 'аппроксимация', 2: 'симацияаппрок', 3: 'квазимногочлен',

            4: 'логнормальный', 5: 'якобиан', 6: 'сюръекция', 7: 'якнаибо', 8: 'невязка'}
for i in range(1, len(anagrams)):
     for j in range(i + 1, len(anagrams)):
          if set(anagrams.get(i)) == set(anagrams.get(j)):
               print(anagrams.get(i), ' is an anagram of ', anagrams.get(j))
