#! python3
# Parsing HTML with BeautifulSoup v4:
#       https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#                       HTML basics:
#                           http://htmldog.com/guides/html/beginner/
#                           http://www.codecademy.com/tracks/web/
#                           https://developer.mozilla.org/en-US/learn/html/

"""
     I shouldn't use Regular Expressions to locate a specific piece of HTML.
     Because HTML can be formatted in many ways and trying to capture all
     these possible variations in a Regular Expression can be tedious and
     error prone.
                                                                            """
# https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

import bs4 # Beautiful Soup v4
import requests

"""
    Beautiful Soup is a module for extracting information from an HTML page
    and is much better for this purpose than Regular Expressions.

    To install it 'pip install beautifulsoup4'
                                                                        """

# Pull weather forecast data from:
# https://www.weather.gov/

# HTML from website:
'''
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text) # bs4.BeautifulSoup needs to be
            # called with a string containg the HTML
'''
# HTML from file:
exampleFile = open('example.html')
noStarchSoup = bs4.BeautifulSoup(exampleFile) # bs4.BeautifulSoup needs to be
            # called with a string containg the HTML

print(type(noStarchSoup))

# finding an element with "select()" Method
    # CSS selector - it is like Regular Expression: specifies a pattern to
        # look for, in HTML pages instead of general text strings.
''' Examples of CSS Selectors:

    soup.select('div')
        All elements named <div>
        
    soup.select('#author')
        The element with an id attribute of author
        
    soup.select('.notice')
        All elements that use a CSS class attribute named notice
        
    soup.select('div span')
        All elements named <span> that are within an element named <div>
        
    soup.select('div > span')
        All elements named <span> that are directly within an element
        named <div>, with no other element in between
        
    soup.select('input[name]')
        All elements named <input> that have a name attribute with any value

    soup.select('input[type="button"]')
        All elements named <input> that have an attribute named type with value button
                                                                            '''
# select() - returns a list of Tag Objects, which is how Beautiful Soup
    # represents an HTML element.
elems = noStarchSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(type(elems[1]))
print(elems[0].getText())
print(elems[1].getText())
print(str(elems[0]))
print(str(elems[1]))
print(elems[0].attrs)
print(elems[1].attrs)

# get() Method for a Tag Objects - gets attribute values from an element.
print(elems[1].get('id')) #(1) it passes a string of an attribute name
            # and returns attribute's value

soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')
span_elems = soup.select('span')[0]
print(str(span_elems))
print(span_elems.get('id')) # like #(1)
print(span_elems.attrs)
