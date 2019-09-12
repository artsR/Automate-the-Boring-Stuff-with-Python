#! python3
# ImageDownloader.py - search category of image and download all.

import os, requests, bs4
import logging

logging.disable()
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

siteUrl = input('Input site\'s url...')
category = input('Input category of searching images...')
findCategory = siteUrl+'/search/?q='+category

print('Loading images with your category on the site: %s...' % findCategory)
res = requests.get(findCategory)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')

#Find all images to download on the site
imagesElem = soup.select('a img')
assert imagesElem != [], 'The images could not be found.'
for element in imagesElem:
    logging.debug('I am inside of the "for" loop.')
    # Find the URL of single image
    imageUrl = 'http:' + element.get('src')
    print('Downloading image %s...' % (imageUrl))

    # Download the image
    res = requests.get(imageUrl)
    assert res.raise_for_status, 'Something wrong with access to: '+str(siteUrl+imageUrl)

    # Save image to folder "./ImageSite"
    print((imageUrl))
    imageFile = open(os.path.join('ImageSite', os.path.basename(imageUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print('Image %s written in the folder' % (imageFile))
    print()

