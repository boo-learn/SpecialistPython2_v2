
students = [('Иванов', 'английский французский'),
            ('Петров', 'английский французский'),
            ('Петров', 'английский'),
            ('Сидоров', 'английский')]


one_lang_students = list(filter(lambda x: len(x[1].split()) == 1, students))
print(*[student[0] for student in one_lang_students])
