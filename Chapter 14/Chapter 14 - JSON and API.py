########## CHAPTER 14 ###########

# JSON - JavaScript Object Notation: popular way to format data as a single
#       human-readable string. JSON is the native way that JS programs write
#       their data structures and usually resembles what Python's pprint()
#       would produce.
#       JSON is very often used as a way for programs to interact with website.
#       (Application Programming Interface (API) )
#
#       Accessing an API is the same as accessing any other web page via a URL.
#       The difference is that the data returned by an API is formatted (w/ JSON)
#       for machines; API aren't easy for people to read.

#       The more info about API on specific website I should look for in
#       documentation provided by this site (usually in 'Developers' page).

# Using API, I could write programs that do the following:
## Scrape raw data from websites (Accessing API is often more convenient than
    #downloading web pages and parsing HTML with bs4 (Beautiful Soup)
## Automatically download new posts from one of my social network accounts and
    #post them to another account (e.x. I could take Tumblr posts to post them
    #to Facebook.
## Create a "movie encyclopedia" for my personal movie collection by pulling
    #data from IMDb, Rotten Tomatoes, and Wikipedia and putting it into a single
    #text file on my computer


'''
https://automatetheboringstuff.com/list-of-json-apis.html


    example of data formatted as JSON:

{"name": "Zophie", "isCat": True, "miceCaught": 0, "napsTaken": 37.5,
"felineIQ": null}
                                                                    '''
# JSON can contain values of only the following data types:
## strings, integers, floats, booleans, lists, dictionaries and NoneType.
#* cannot represent Python-specific objects like: File object, CSV reader etc..

import json

# Reading JSON with the 'loads()'
stringJSONdata = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringJSONdata)
print(jsonDataAsPythonValue)

# Writing JSON with the 'dumps()'
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
JSONformat = json.dumps(pythonValue)# conver data to be understandable for JavaScript
print(JSONformat)

