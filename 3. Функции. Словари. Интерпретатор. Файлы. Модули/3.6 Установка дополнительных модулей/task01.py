import requests

with open('dataset_3378_2.txt') as inf:
    link = inf.read().strip()
r = requests.get(link)
print(r.text.count('\n'))
