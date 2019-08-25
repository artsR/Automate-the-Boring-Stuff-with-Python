import re

strongPassRegex = re.compile(r'''(
    ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([a-zA-Z\d]{8,})$ # I don't understand "?="    
    )''', re.VERBOSE)

try:
    mo = strongPassRegex.search('dobryPass8').group()
    print(mo)
except:
    print('It\'s NOT STRONG password')

################################################################################

def check_pass(text):
    """
    Returns a boolean indicating if the password is strong
    Strong passwords are 8 characters or longer,
    contain at least one uppercase letter,
    lowercase letter and digit.
                                                        """

    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    lengthRegex = re.compile(r'.{8,}')
    digitRegex = re.compile(r'\d')

    if not upperRegex.search(text):
        return False
    elif not lowerRegex.search(text):
        return False
    elif not lengthRegex.search(text):
        return False
    elif not digitRegex.search(text):
        return False
    else:
        return True

if check_pass('dobryPass8'):
    print('dobryPass8')
else:
    print('It\'s NOT STRONG password')


    
        
    
