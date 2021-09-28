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