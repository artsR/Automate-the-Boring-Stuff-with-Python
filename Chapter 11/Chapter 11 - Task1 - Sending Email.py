#! python3
# send_email.py - Program takes:
#                       1. email address from command line
#                       2. text which will be send to this email address
#               then it logs into my email account and sends mentioned message.

import sys, pyperclip, time
from selenium import webdriver

if len(sys.argv) > 2:
    address_email = sys.argv[1]
    text_to_send = ' '.join(sys.argv[2:])
else:
    text_to_send = pyperclip.paste()

browser = webdriver.Firefox()
browser.get('https://www.poczta.onet.pl')

try:
    email_login = browser.find_element_by_id('f_login')
    email_login.send_keys('blabla@op.pl')
    print('Element %s found' % (email_login.tag_name))
except:
    print('Element not found' % (email_login.tag_name))
try:
    email_passwd = browser.find_element_by_id('f_password')
    email_passwd.send_keys('blabla')
    print('Element %s found.' % (email_passwd.tag_name))
except:
    print('Element not found.' % (email_passwd.tag_name))
email_passwd.submit()
time.sleep(5)
advertisingClose = browser.find_element_by_css_selector('.cmp-button_button.cmp-intro_acceptAll')
advertisingClose.click()
#NewEmail = browser.find_element_by_link_text('Napisz wiadomość')
NewEmail = browser.find_element_by_id('NewMail-button')
NewEmail.click()
time.sleep(5)
sendEmail = browser.find_element_by_id('newmail-txtmailto-multipleInput')
print('I\'m introducing recipient...')
sendEmail.send_keys(address_email)
print('Email topic is creating...')
inputTopic = browser.find_element_by_id('newmail-subject')
inputTopic.send_keys('My first email sent automatically')
emailContent = browser.find_element_by_id('newmail-editor_ifr') #xpath("/html/body[@id='tinymce']/dev")
print('I\'m writing email messsage...')
emailContent.send_keys(text_to_send)
time.sleep(5)
sendingEmail = browser.find_element_by_id('newmail-actions-top-send').click()
print('Email sent.')
time.sleep(10)
browser.close()
