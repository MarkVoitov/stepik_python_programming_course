n = int(input())
s = [0, 0]

for line in range(n):
    directions = []
    direction = [i for i in input().split('\n')]
    direction = ''.join(direction).split()
    directions.append(direction)
    directions = sum(directions, [])
    if directions[0] == 'север':
        s[1] += int(directions[1])
    elif directions[0] == 'юг':
        s[1] -= int(directions[1])
    elif directions[0] == 'запад':
        s[0] -= int(directions[1])
    elif directions[0] == 'восток':
        s[0] += int(directions[1])    

for coord in s:
    print(coord, end=' ')