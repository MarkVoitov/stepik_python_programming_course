x = input().lower()
count = 0

for i in x:
    if i == 'g':
        count += 1
    if i == 'c':
        count += 1
print(count / len(x) * 100)