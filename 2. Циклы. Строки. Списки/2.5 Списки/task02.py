a = [int(i) for i in input().split()]
total = []
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i == 0:
            total.append(a[1] + a[-1])
        elif i == (len(a) - 1):
            total.append(a[-2] + a[0])
        else:
            total.append(a[i - 1] + a[i + 1])
    for i in total:
        print(i, end=' ')