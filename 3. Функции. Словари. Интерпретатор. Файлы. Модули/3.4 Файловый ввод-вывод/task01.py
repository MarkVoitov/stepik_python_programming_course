with open('dataset_3363_2.txt') as doc:
    line = doc.read()
    symbols, numbers = [], []
    number = ''
    for i in line:
        if i.isdigit():
            number += i
        else:
            if number != '':
                numbers.append(int(number))
                number = ''
            if not i.isdigit():
                symbols.append(i)
                
    if number != '':
        numbers.append(int(number))

final_list = [symbol * number  for symbol, number in zip(symbols, numbers)]
final_list = (''.join(final_list))

with open('dataset_3363_2.txt', 'w') as doc:
    doc.write(final_list)
    
