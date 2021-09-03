fig = input()
if fig == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif fig == 'прямоугольник':
    a = int(input())
    b = int(input())    
    print(a * b)
elif fig == 'круг':
    r = int(input())
    print(3.14 * (r ** 2))