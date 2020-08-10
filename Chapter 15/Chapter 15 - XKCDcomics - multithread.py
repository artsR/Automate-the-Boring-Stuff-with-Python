#! python3
# XKCD_multithreading.py - Downloads XKCD comics using multiple threads.


import os, requests, bs4, threading

os.makedirs('XKCD - multithread', exist_ok=True) # store comics in ./XKCD - multithread

def downloadXKCD(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page:
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        # Find the URL of the comic image:
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image:
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('http:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./XKCD - multithread:
            imageFile = open(os.path.join('XKCD - multithread',
                                          os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects:
downloadThreads = [] # a list of all the Tread objects
for i in range(0, 50, 10):
    downloadThread = threading.Thread(target=downloadXKCD, args=(i, i+9))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end:
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

    
