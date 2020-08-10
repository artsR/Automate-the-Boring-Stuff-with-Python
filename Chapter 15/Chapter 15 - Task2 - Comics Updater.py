#! python3
# comicsUpdater.py - Checks if the new image was added and then downloads it.

import os, shelve, requests, bs4

def checksUpdates (site, link):
    shelfFile = shelve.open('updateStatus', writeback=True)
    
    if shelfFile['updater'][site]['link'] == link:
        return 1
    else:
        shelfFile['updater'][site]['link'] = link
        return 0

comicsSites = [['http://xkcd.com','comic',0,''],
               ['http://www.lefthandedtoons.com','comicwrap',3,''],
               ['http://buttersafe.com','comic',0,''],
               ['https://www.savagechickens.com','theloop',0,''],
               ['http://www.lunarbaboon.com','item36152153',1,'lunarbaboon'],
               ['http://completelyseriouscomics.com','comic',0,''],
               ['https://www.exocomics.com','comic-1952',0,''],
               ['http://nonadventures.com','comic',0,''],
               ['https://moonbeard.com','comic',0,''],
               ['http://www.happletea.com','comic',0,'']]
os.makedirs('Chapter 15 - comics', exist_ok=True)
folder = os.path.abspath('Chapter 15 - comics')
linking = []
for site in comicsSites:
    print('Checking website:  %s' % (site[0]))
    res = requests.get(site[0])
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="lxml")

    # Find the URL of the comic image:
    comicElem = soup.select('#'+site[1]+' img')
    if comicElem == []:
        print('Image no found.')
    else:
        comicUrl = comicElem[site[2]].get('src')
        # Setting full image address:
        if 'http' in comicUrl:
            link = comicUrl            
        elif comicUrl.startswith('//'):
            link = ('http:' + comicUrl)
        else:
            link = (site[0] + comicUrl)
        if checksUpdates(site[0], link) == 1:
            print('You have the newest episode of comic.')
            continue
        # Download image:
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(link)
        res.raise_for_status()
        # Save the image to 'Chapter 15 - comics':
        if site[3] == '':
            imageFile = open(os.path.join(folder, os.path.basename(comicUrl)),'wb')
        else:
            imageFile = open(os.path.join(folder, site[3]),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
               
