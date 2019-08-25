import re

thou = re.compile(r'^\d{1,3}(,\d{3})*$')
try:
    mo = thou.search('1,0').group()
    print(mo)
except:
    print('Not founded.')


surRegex = re.compile(r'[A-Z][a-zA-Z]+\sNakamoto$')
mo = surRegex.search('Satoshi Nakamoto').group()
print(mo)


senRegex = re.compile(r'''(
    ^(Alice|Bob|Carol)\s
    (eats|pets|throws)\s
    (apples|cats|baseballs)
    ((\s|,\s).*)?
    (\.$)
    )''', re.VERBOSE | re.IGNORECASE | re.DOTALL)
try:
    mo = senRegex.search('Carol eats cats, and dogs.').group()
    print(mo)
except:
    print('No founded')
