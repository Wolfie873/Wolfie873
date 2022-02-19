#! python3
from pickle import TRUE
from turtle import clear
import copy #Imports the copy function

animals = ['cow', 'horse', 'pig', 'cat', 'dog'] #This is a list of strings
print(animals.index('pig')) #Prints the index number where the string is located
animals.append('hyena') #Appends a value at the end of a list
print(animals)
for i in range(len(animals)): #A loop based on the size of the list
    print(animals[i])
animals.insert(0, 'kingcow') #Inserts a new value at (index number, value to add). Moves values one place, does not delete
print(animals)
del animals[1] #Deletes the value at [index number]
print(animals)
animals.remove('hyena') #Looks for and removes the value in the list
print(animals)

games = ['halo', 'pokemon', 'call of duty', 'pokemon', 'star wars', 'pokemon'] #List where multiple values repeat
games.remove('pokemon') #This method only removes the first value it finds of this type on the list
print(games)

numbers = [2,5,3,1,7,9]
numbers.sort() #Sort numbers list ascending
for i in range(len(numbers)): #A loop based on the size of the list
    print(numbers[i])

animals.sort() #Sort animations list alphabetically
print(animals)
animals.sort(reverse=True) #Reverse sort
print(animals)
#Can't sort lists with int and str in same list
#Sorts in ASCII-phetical order. Meaning all the uppercase characters come before lowercase.

lowerfirst = ['Area', 'area', 'Beach', 'beach', 'raviolli', 'Pizza']
lowerfirst.sort(key=str.lower) #This method sorts by true alphabetical order by conventing all strings into lowecase first
for i in range(len(lowerfirst)):
    print(lowerfirst[i])

print(list('Hello')) #Makes a list of each letter for the string

name = 'Jorge Ortiz' #Most functions you can use on lists, you can also use on strings
print(name[0])
print(name[1:3])
print(name[-3])
for letter in name:
    print(letter)
newName = name[:6] + 'the ' + name[6:] #With slicing you can manipulate text, as it is an immutable object
print(newName)

mutableList = [1, 2, 3, 4, 5, 6]
changedList = mutableList #This creates a reference to the list above
print(changedList)
changedList[1] = 'Hello'
print(changedList)
print(mutableList)
#Lists are mutable objects and as such can be changed with the reference. They are the same lost

def eggs(someParameter):
    someParameter.append('Eggs n\' Bakey')
eggnum = [1, 2, 3]
eggs(eggnum)
print(eggnum)

spam = [1, 2, 3, 4, 5]
cheese = copy.deepcopy(spam) #Creates a copy of the list that does not modify original list
print(cheese)
pokes = ['charmander', 'squirtle', 'bulbasaur']
cheese.append(pokes[1])
print(spam)
print(str(cheese))
 #Python does not care for indentations as long as these methods are used
speech = 'Four score and ' + \
    'seven years ago, the forefathers of this nation' + \
        ' I am so fucking high right now.'
print(speech)
alsoSpeech = ['Maybe', 
              'Yes', 
              'Perhaps']
print(alsoSpeech)