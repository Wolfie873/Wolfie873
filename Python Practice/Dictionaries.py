#! python3
#Dictonaries can contain more than one type of variable and are set up as dic = {'key': 'value'}
from token import NEWLINE


myDog = {'color': 'brown', 'size':'medium', 'weight': 'normal'}
print('My dog is ' + myDog['color'])
keyEx = {12345: 'Password information', 34: 'Name'}
print(keyEx[34])
#Dictonaries have no order. If two dictonaries contain the same values Python considers them the same
keyXe = {34: 'Name', 12345: 'Password information'}
print(keyXe == keyEx)
print(list(keyEx.keys())) #Lists the individual keys in the same line
print(list(keyXe.values())) #Lists the individual values in the same line
print(list(keyXe.items())) #Lists the items which is both key and vale in the same line

for k in keyXe.keys(): #Saves the key values to the k variable and prints them out in new lines
    print(k)
for v in keyXe.values(): #Saves the values to the v variable and prints them out in new lines
    print(v)
for k, v in keyXe.items(): #Saves the key and value into the corresponding variable and prints them out in new lines
    print(k, v)
for i in keyXe.items(): #Same as above but displays them within parenthesis
    print(i)
#The get(key, defaultvalue) method
print(myDog)
print(myDog.get('color', 0))
print(myDog.get('age', 0))
#The setdefault(key, defaultvalue) method
print(myDog)
myDog.setdefault('age', 21)
print(myDog['age'])