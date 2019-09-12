#! python3
# googleSearch.py - Opens several Google search results.

import sys, webbrowser, requests, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


# The program can also do the following:
## Open all the product pages after searching a shopping site such as Amazon
## Open all the links to reviews for a single product
## Open the result links to photos after performing a search on a photo
    ## site such as Flickr or Imgur
