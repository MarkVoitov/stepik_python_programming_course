input_line, output_line, encode_line, decode_line = list(input()), list(input()), list(input()), list(input())

encoder = dict(zip(input_line, output_line))

encode_list = []
for i in encode_line:
    if i in encoder:
        encode_list.append(encoder[i])

decode_list = []
for i in decode_line:
    for key, value in encoder.items():
        if value == i:
            decode_list.append(key)
            
for i in encode_list:
    print(i, end='')
    
print('')

for i in decode_list:
    print(i, end='')