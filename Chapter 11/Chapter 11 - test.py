#! python3

import requests, bs4

res = requests.get('http://www.onet.pl')
res.raise_for_status()
print(res.status_code)

onetFile = open('ONETpl.txt', 'wb')
for chunk in res.iter_content(100000):
    print(onetFile.write(chunk))
onetFile.close()
#print(res.text)
onetSoup = bs4.BeautifulSoup(res.text, features='html.parser')




