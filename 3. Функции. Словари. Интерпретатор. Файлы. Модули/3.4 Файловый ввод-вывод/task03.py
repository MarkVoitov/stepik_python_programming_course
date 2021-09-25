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