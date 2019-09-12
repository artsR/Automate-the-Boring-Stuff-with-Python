# selenium Module

# It is able to do sophisticated tasks e.x. log in on the page..
#                                  https://selenium-python.readthedocs.io/

from selenium import webdriver # importing selenium Module

browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')

# Finding elements on a page:
## find_element_*   method - returns a single WebElement Object
## find_elements_*  method - returns a list of WebElement_* Objects
    # if no elements exist on the page, the selenium module raises NoSuchElement
    # exception and the program crashs (to avoid it I should use "try,except")
""" A few examples:

    https://gyazo.com/c8562f82609a3ed0449e8e02a5a5ab23

                WebElement Attributes and Methods
                
  Attribute or method                   Description
    tag_name              The tag name, such as 'a' for an <a> element
    get_attribute(name)   The value for the element’s name attribute
    text                  The text within the element, such as 'hello'
                          in <span>hello</span>
    clear()               For text field or text area elements,
                          clears the text typed into it
    is_displayed()        Returns True if the element is visible;
                          otherwise returns False
    is_enabled()          For input elements, returns True if the element is
                          enabled; otherwise returns False
    is_selected()         For checkbox or radio button elements,
                          returns True if the element is selected;
                          otherwise returns False
    location              A dictionary with keys 'x' and 'y' for the position of
                          the element in the page
                                                                            """
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
    
# Clicking the page
linkElem = browser.find_element_by_link_text('Forum')
print(type(linkElem))
linkElem.click()    # follows the "Forum" link. Simulates mouse clicking

browser.get('https://gmail.com')
try:
    emailElem = browser.find_element_by_id('Email')
    emailElem.send_keys('fake_email@gmail.com')
    passwordElem = browser.find_element_by_id('Passwd')
    passwrodElem.send_keys('12345')
    passwordElem.submit()
except:
    print('Elements no founded')
    
# Sending Special Keys
"""
            Attributes                             Meanings
            
    Keys.DOWN, Keys.UP, Keys.LEFT,          The keyboard arrow keys
        Keys.RIGHT

    Keys.ENTER, Keys.RETURN                 The enter and return keys
    Keys.HOME, Keys.END, Keys.PAGE_DOWN,    The home, end, pagedown, and pageup keys
        Keys.PAGE_UP                            

    Keys.ESCAPE, Keys.BACK_SPACE,           The esc, backspace, and delete keys
        Keys.DELETE

    Keys.F1, Keys.F2, ... , Keys.F12        The F1 to F12 keys at the top of the keyboard

    Keys.TAB                                The tab key
                                                                            """

# to run the special keys I need to:
## 'from selenium.webdriver.common.keys import Keys'
## and then run e.x. : 'object.send_keys(Keys.DOWN)'
    # OR
## I may run e.x.  : 'webdriver.common.keys(Keys.DOWN)
from selenium.webdriver.common.keys import Keys
browser.get('http://nostarch.com')
# the <html> tag contains full content of the HTML file(page). It is good place
    # send keys to the general web page.
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)    # scrolls the page to bottom
htmlElem.send_keys(Keys.HOME)   # scrolls the page to top

# Clicking browser Buttons
## browser.back()       Clicks the Back button
## browser.forward()    Clicks the Forward button
## browser.refresh()    Clicks the Refresh button
## browser.quit()       Clicks the Close Window button
