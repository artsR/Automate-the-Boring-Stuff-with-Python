import shelve

comic = [   ['http://xkcd.com','comic',0,''],
            ['http://www.lefthandedtoons.com','comicwrap',3,''],
            ['http://buttersafe.com','comic',0,''],
            ['https://www.savagechickens.com','theloop',0,''],
            ['http://www.lunarbaboon.com','item36152153',1,'lunarbaboon'],
            ['http://completelyseriouscomics.com','comic',0,''],
            ['https://www.exocomics.com','comic-1952',0,''],
            ['http://nonadventures.com','comic',0,''],
            ['https://moonbeard.com','comic',0,''],
            ['http://www.happletea.com','comic',0,'']]

link = ['http://imgs.xkcd.com/comics/sharing_options.png', 'http://www.lefthandedtoons.com/toons/drew_ariotheory.gif', 'http://buttersafe.com/comics/2019-01-31-IFinallyFound.jpg', 'https://www.savagechickens.com/wp-content/uploads/chickenshortwinters.jpg', 'http://www.lunarbaboon.com/storage/comicrecommend.jpg?__SQUARESPACE_CACHEVERSION=1548597706547', 'http://completelyseriouscomics.com/comics/2015-12-08-how%20to%20end%20a%20webcomic.jpg', 'https://www.exocomics.com/wp-content/uploads/549.jpg', 'http://nonadventures.com/comics/2019-01-01-478.png', 'https://moonbeard.com/comics/2019-02-01-Box-Of-Spiders.png', 'http://www.happletea.com/wp-content/uploads/03-02-2018.jpg']

shelfFile = shelve.open('updateStatus')
s = shelfFile['updater']

for i in range(10):
    print(s[comic[i][0]]['link'], end='... ')
    print(s[comic[i][0]]['link'] == link[i])



