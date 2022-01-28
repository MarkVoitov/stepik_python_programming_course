# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

# Попробуем написать подобную систему.

# На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова.
# Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

# Sample Input:
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic

# Sample Output:
# stepic
# champignons
# the




d = int(input())
d_words = []
for word in range(d):
    word = [i for i in input().lower().split('\n')]
    d_words.append(word)
d_words = sum(d_words, [])
d_words = set(d_words)

l = int(input())
l_texts = []
for text in range(l):
    text = [i for i in input().lower().split('\n')]
    text = ''.join(text).split()
    l_texts.append(text)
l_texts = sum(l_texts, [])
l_texts = set(l_texts)

output = l_texts.difference(d_words)
for word in output:
    print(word)
