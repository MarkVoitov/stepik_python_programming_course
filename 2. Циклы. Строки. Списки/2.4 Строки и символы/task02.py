s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    if s[i] != s[i + 1]:
        count += 1
        print(s[i], end='')
        print(count, end='')
        count = 0
print(s[-1], end='') 
print(count + 1, end='')