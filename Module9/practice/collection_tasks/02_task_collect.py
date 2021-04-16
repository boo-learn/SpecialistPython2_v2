# Каждый ученик в классе изучает либо английский, либо французский, либо оба этих языка.
# У классного руководителя есть списки учеников, изучающих английский и французский языки.
# Помогите ему выяснить, сколько учеников в классе изучают только один язык.

# Входные данные:
# Для каждого ученика известны: Имя Фамилия и список изучаемых языков

# Для решения задачи подберите наиболее удобную структуру и заполните
# Выведите: учеников, изучающих только один язык


from collections import Counter


students = [
    {'name': 'Вася', 'surname': 'Пупкин', 'languages': ['english', 'french']},
    {'name': 'Женя', 'surname': 'Скарибидис', 'languages': ['english', ]},
    {'name': 'Петя', 'surname': 'Пёс', 'languages': ['french', ]},
    {'name': 'Эмиль', 'surname': 'Гусейнов', 'languages': ['english', ]},
    {'name': 'Витя', 'surname': 'Евстафьев', 'languages': ['english', 'french']},
    {'name': 'Саша', 'surname': 'Лищенко', 'languages': ['french', ]},
    {'name': 'Серёга', 'surname': 'Кувалда', 'languages': ['english', ]},
    {'name': 'Маша', 'surname': 'Загорская', 'languages': ['english', 'french']},
    {'name': 'Кристина', 'surname': 'Шаманова', 'languages': ['english', ]},
    {'name': 'Данил', 'surname': '1JZ-GE', 'languages': ['html']},  # Что-то настроение хорошее))
]

def count_single_language_students(students):
    counter = Counter()
    for student in students:
        languages = student['languages']
        if len(languages) == 1:
            counter[languages[0]] += 1
    return counter


if __name__ == '__main__':
    print('Иностранные языки у учеников')
    counter = count_single_language_students(students)
    res = ''
    single_languaged = 0
    for c in counter.most_common():
        single_languaged += c[1]
        res += f'язык: {c[0]} учеников: {c[1]}\n'
    print(f'Среди учеников изучают один язык: {single_languaged}\n' + res)
