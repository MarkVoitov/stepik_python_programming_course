a = float(input())
b = float(input())
x = input()

if x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif x == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif x == '*':
    print(a * b)
elif x == 'mod':
    print(a % b)
elif x == 'pow':
    print(a ** b)
elif x == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')