from socket import if_nameindex
from tkinter import TRUE


dog = {'name': 'Chewie', 'age': 3, 'color': 'brown'}
allDogs = []
allDogs.append({'name': 'Chewie', 'age': 3, 'color': 'brown'})
allDogs.append({'name': 'Leia', 'age': 2, 'color': 'white'})
allDogs.append({'name': 'Solo', 'age': 1, 'color': 'white'})
allDogs.append({'name': 'Minnie', 'age': -5, 'color': 'black'})
print(allDogs)

print(type(42))
print(type('hello'))
print(type(if_nameindex))