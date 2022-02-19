import pyperclip

text = 'Hello World!'
print(text.upper()) #Uppercase all letters
print(text.lower()) #Lowercase all letters
print(text.islower()) #True if all lowercase
print(text.isupper()) #True if all uppercase
print(text.lower().islower()) #Converts lowercase and asks if true
print(text.isalpha())
print('\n\n'.join(['cats', 'bats', 'rats'])) #Joins strings on a list together with specified characters
print(text.split('l')) #Splits the string into a list on specified character
print('Hello'.rjust(10, '*')) #Adds as many characters to the right of the string as stated
print('Hiya'.ljust(10, '-')) #Same with the left of the string
print('Hi'.center(10)) #Centers the string based on specified characters
name = 'Jorge'
print(name.center(10, '='))
more = 'Nother!'
print(more.center(50))
moreR = more.rjust(10)
print(moreR.strip()) #Strips white space
repeat = 'Many Many Many More People Many Dude Many'.replace('a', 'o') #Replaces all A with O in the string
print(repeat)