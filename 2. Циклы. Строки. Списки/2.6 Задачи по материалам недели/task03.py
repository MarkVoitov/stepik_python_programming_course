lst = [int(i) for i in input().split()]
x = int(input())
ouput_lst = []

for i in range(len(lst)):
    if lst[i] == x:
        ouput_lst.append(i)
        
if len(ouput_lst) != 0:
    print(*ouput_lst)
else:
    print('Отсутствует')