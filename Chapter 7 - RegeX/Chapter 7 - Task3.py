import re


def regex_strip(text, item=None):

    if item == None:
        textRegex = re.compile(r'\w+.*\w')  # I don't get it why it works for
        new_text = textRegex.search(text)   # '      hello  city   corn   '
    else:                                   # It works because there is '.*'
        textRegex = re.compile(item)
        new_text = textRegex.sub('', text)
    return new_text

print(regex_strip('      hello  city   corn   '))
