a = [int(i) for i in input().split()]
a.sort()

total = []
for i in a:
    if a.count(i) > 1:
        total.append(i)

total_unique = []
for i in total:
    if i in total_unique:
        continue
    else:
        total_unique.append(i)

for i in total_unique:
    print(i, end=' ')