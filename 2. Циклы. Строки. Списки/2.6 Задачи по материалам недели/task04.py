a = []
b = input()
while b != "end":
    a.append(b.split())
    b = input()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(int(a[i-1][j]) + int(a[i-len(a)+1][j]) + int(a[i][j-1]) + int(a[i][j-len(a[i])+1]), end =" ")
    print()