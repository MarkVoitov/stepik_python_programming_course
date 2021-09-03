a = int(input())
b = int(input())
c = int(input())

if a < b:
    a, b = b, a
elif a < c:
    a, c = c, a
elif b > c:
    b, c = c, b
print(a)
print(b)
print(c)