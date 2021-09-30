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