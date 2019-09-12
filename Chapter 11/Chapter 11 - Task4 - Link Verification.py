#! python3
# link_verification.py

import requests, bs4

websiteUrl = 'http://nostarch.com'
res = requests.get(websiteUrl)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
#linksElem = soup.find_all("a", href=True)  #found 162 elements
#linksElem = soup.select('a[href!=""]')     #found 163 elements
linksElem = soup.select('a[href]')          #found 162 elements
counter = 0
for link in linksElem:
    print(str(counter)+'--------------------------------------------------')
    print('link = ', str(link))
    print('href of link = ' + str(link.get('href')))
    if 'http' in link.get('href'):
        linkUrl = link.get('href')
    elif link.get('href').startswith('/'):
        linkUrl = requests.get(websiteUrl + link.get('href'))
    else:
        linkUrl = requests.get(websiteUrl + '/' + link.get('href'))
    print('linkUrl = ' + str(linkUrl))
    try:
        linkUrl.raise_for_status()
    except Exception as exc:
        print('There was a problem %s with the link: %s' % (exc, linkUrl))
    counter += 1
print('Verification terminated.')


