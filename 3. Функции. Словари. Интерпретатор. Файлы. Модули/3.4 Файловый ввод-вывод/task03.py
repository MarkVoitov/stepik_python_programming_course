# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

# Поля внутри строки разделены точкой с запятой, оценки — целые числа.

# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.

# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения,
# разделённые пробелом, последней строкой в файл с ответом.

# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.

# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']

# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667




with open('dataset_3363_4.txt') as doc:
    total_list = []
    for line in doc:
        line = line.strip().split(';')
        total_list.append(line)

grade_student, math_list, phis_list, lang_list = [], [], [], []
grade = 0
for i in total_list:
    grade = (int(i[1]) + int(i[2]) + int(i[3])) / 3
    grade_student.append(grade)
    math_list.append(int(i[1]))
    phis_list.append(int(i[2]))
    lang_list.append(int(i[3]))    

total_grades = [sum((math_list)) / len(math_list), sum((phis_list)) / len(phis_list), sum((lang_list)) / len(lang_list)]

with open('dataset_3363_4.txt', 'w') as doc:
    for grade in grade_student:
        doc.write(str(grade) + '\n')
    for total_grade in total_grades:
        doc.write(str(total_grade) + ' ')
