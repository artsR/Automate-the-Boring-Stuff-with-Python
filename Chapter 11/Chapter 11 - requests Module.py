#! python3

import requests # https://requests.readthedocs.io/en/master/

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status() # raises Exception if there was an error downloading file
except Exception as exc:
    print('There was a problem: %s' % (exc))
print(type(res)) # return a Response Object, which contains the response that
    # that the web server gave for my request.

res.status_code == requests.codes.ok
print(len(res.text))
print(res.text[:250])


# Unicode Encodings:
## https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
## https://nedbatchelder.com/text/unipain.html

# Saving Downloaded Files to the Hard Drive
## open file with write binary mode ('wb') in order to maintain Unicode encoding
## write
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk)) # returns number of bytes written to the file.

playFile.close()

## TODO write onet.pl to txt
