# Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

# На ввод могут подаваться и повторяющиеся числа.

# Sample Input 1:
# 8
# 2
# 14
# Sample Output 1:
# 14
# 2
# 8

# Sample Input 2:
# 23
# 23
# 21
# Sample Output 2:
# 23
# 21
# 23





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
