# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".

# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/

# Загрузите содержимое последнего файла из набора, как ответ на это задание.




import requests

with open('dataset_3378_3.txt') as inf:
    link = inf.read().strip()

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
while True:
    r = requests.get(link)
    if str(r.text).strip().split()[0] == 'We':
        break
    link = url + str(r.text)

with open('dataset_3378_3.txt', 'w') as ouf:
    ouf.write(r.text)
