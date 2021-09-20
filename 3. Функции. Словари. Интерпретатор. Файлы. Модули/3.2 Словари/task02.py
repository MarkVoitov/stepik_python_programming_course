x = [i.lower() for i in input().split()]
d = {}

for i in x:
    total = x.count(i)
    if i not in d:
        d[i] = total
        
for key, value in d.items():
    print(key, value)