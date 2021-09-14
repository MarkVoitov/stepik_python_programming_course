n = int(input())
list = []
sum_list = []

for i in range(1, n + 1):
    list = [i]
    sum_list += (i * list)

for i in sum_list[:n]:
    print(i, end=' ')