#! python3
from ctypes.wintypes import HDC
import re

teststring = 'This is a text string with two phone numbers and two other things '\
    '234-837-2883 and 455-382-8574 and 334432-35533-2 theres also 4334-32-3455'
#message = input('Please enter your text here: ')

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegEx.findall(teststring)
print(mo)