#Dictonaries can contain more than one type of variable and are set up as dic = {'key': 'value'}
from token import NEWLINE


myDog = {'color': 'brown', 'size':'medium', 'weight': 'normal'}
print('My dog is ' + myDog['color'])
keyEx = {12345: 'Password information', 34: 'Name'}
print(keyEx[34])
#Dictonaries have no order. If two dictonaries contain the same values Python considers them the same
keyXe = {34: 'Name', 12345: 'Password information'}
print(keyXe == keyEx)
print(list(keyEx.keys()))
print(list(keyXe.values()))
print(list(keyXe.items()))

for k in keyXe.keys():
    print(k)
for v in keyXe.values():
    print(v)
for k, v in keyXe.items():
    print(k, v)