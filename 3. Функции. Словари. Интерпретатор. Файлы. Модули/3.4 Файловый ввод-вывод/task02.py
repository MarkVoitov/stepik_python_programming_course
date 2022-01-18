# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то,
# сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3




with open('dataset_3363_3.txt') as doc:
    words_list = doc.read().lower().strip().split()
    
words_list.sort()
word_dict = {}

for i in words_list:
    total = words_list.count(i)
    if i not in word_dict:
        word_dict[i] = total

final_list = []    
for x in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
    final_list.append((x[0], x[1]))
print(final_list[0][0], final_list[0][1])
