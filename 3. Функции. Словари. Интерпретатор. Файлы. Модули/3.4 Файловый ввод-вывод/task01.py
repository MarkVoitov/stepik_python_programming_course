# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset".
# Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
# Запустите вашу программу, используя этот файл в качестве входных данных.
# Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb




with open('dataset_3363_2.txt') as doc:
    line = doc.read()
    symbols, numbers = [], []
    number = ''
    for i in line:
        if i.isdigit():
            number += i
        else:
            if number != '':
                numbers.append(int(number))
                number = ''
            if not i.isdigit():
                symbols.append(i)
                
    if number != '':
        numbers.append(int(number))

final_list = [symbol * number  for symbol, number in zip(symbols, numbers)]
final_list = (''.join(final_list))

with open('dataset_3363_2.txt', 'w') as doc:
    doc.write(final_list)
