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