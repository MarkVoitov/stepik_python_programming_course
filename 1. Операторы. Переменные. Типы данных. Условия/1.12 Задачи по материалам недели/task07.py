x = input()
x = int(x)
sixth = x % 10
fifth = x % 100 // 10
fourth = x % 1000 // 100
third = x % 10000 // 1000
second = x % 100000 // 10000
first = x % 1000000 // 100000

if first + second + third == fourth + fifth + sixth:
    print('Счастливый')
else:
    print('Обычный')