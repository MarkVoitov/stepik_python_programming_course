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