########### CHAPTER 16 ############


# Sending Emails:

import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.poczta.example.pl', 465) #address smtp and port
# smtplib.SMTP('smtp.address', 587)
# smtplib.SMTP_SLL('smtp.address', 465)
smtpObj.ehlo() # Establishing connection to the server. Returns 220 if server
#               is ready.
#smtpObj.starttls() # Enables encryption TLS for my connection.
# for SLL encryption is already set up so I don't have to do it again.
smtpObj.login('example@example.pl', 'somepassword') # Returns 235 if authentication
#           was successful.
#smtpObj.sendmail('example@op.pl', 'examples@op.pl',
#                 'Subject: First mail by smtp\n...mail...') # from, to, mail
smtpObj.quit() # Returns 221 if session was ended successfuly.

'''
            Provider                  SMTP server domain name
    
        Gmail                      smtp.gmail.com (587)
        Outlook.com/Hotmail.com    smtp-mail.outlook.com (587)
        Yahoo Mail                 smtp.mail.yahoo.com (587)
        AT&T                       smpt.mail.att.net (port 465)
        Comcast                    smtp.comcast.net (587)
        Verizon                    smtp.verizon.net (port 465)
                                                                    '''

# Receiving Emails:

import imapclient, pprint
# http://imapclient.readthedocs.org/

imapObj = imapclient.IMAPClient('imap.poczta.example.pl', ssl=True)
imapObj.login('example@example.pl', 'somepassword')
pprint.pprint(imapObj.list_folders()) # list of the folders in EMAIL.
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL']) # for gmail.com I may use 'imapObj.gmail_search'
#                           it is more advanced and sophisticated.
print(UIDs)
rawMessages = imapObj.fetch([47], [b'BODY[]', 'FLAGS'])
#rawMessages = imapObj.fetch(UIDs, [b'BODY[]', b'FLAGS'])
pprint.pprint(rawMessages)


''' SEARCH arguments for 'search()' Method

https://gyazo.com/c6a39b7b17fb27b19dee0ac560a30832
https://gyazo.com/7c952643a5a9a33e105a2d4f3151de00
'''


import pyzmail # convert receive email by imap to the simple string.
#               http://www.magiksys.net/pyzmail/

message = pyzmail.PyzMessage.factory(rawMessages[47][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))
if message.text_part != None: # if == None - email is only HTML code
    print(message.text_part.get_payload())
# .decode(message.text_part.charset) - argument is message's character encoding
#    print(message.text_part.get_payload().decode(message.text_part.charset))
if message.html_part != None: # if == None - email is only PLAINTEXT
    #print(message.html_part.get_payload())
    myEmail = message.html_part.get_payload().decode(message.html_part.charset)
    print(message.html_part.get_payload().decode(message.html_part.charset))# - argument is message's character encoding 
#    print(message.html_part.get_payload().decode(message.html_part.charset))

# Deleting emails:
print(UIDs[6])
imapObj.delete_messages(UIDs[6])# tagged choisen message as 'deleted'
imapObj.expunge() # permanently remove all emails with the tag 'deleted'
#                   in the currently selected folder.
imapObj.logout()

import imaplib

#imaplib._MAXLINE = 10000000 # Changes size limit of bytes for email message.


# Scanning email content to find links:
import bs4

soup = bs4.BeautifulSoup(myEmail, features="lxml")
link = soup.select('img')
pprint.pprint(link)
