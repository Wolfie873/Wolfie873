#! python3
#Above is the Shebang Line which tells Windows which version of python to run. Should be at the top of all python files.
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
pyperclip.copy(text)
print(pyperclip.paste())

#String formatting is very useful and important
name = 'Jorge'
age = '27'
weakness = 'Pizza Pie'
strength = 'Apple Computer Software'
birtday = '10/12/20'

print('Hello %s I know you are %s and there are many things you want '\
    'to know about your weakness %s and I know your one true '\
        'strength %s you were born on %s.' % (name, age, weakness, strength, birtday))