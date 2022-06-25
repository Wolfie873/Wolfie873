#! python 3
import re
from signal import pause

beginsWithHello = re.compile(r'^Hello')

print(beginsWithHello.search('Hello there!'))

endsWithWorld = re.compile(r'world!$')

print(endsWithWorld.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+\w\d+$')

print(allDigitsRegex.search('1234x567890'))

atRegex = re.compile(r'.at')

print(atRegex.findall('The cat in the hat sat patiently with the rat and the bat next to the mat.'))

nameRegex = re.compile(r'[f|F][i|I][r|R][s|S][t|T].[n|N][a|A][m|M][e|E].\s(.*) [l|L][a|A][s|S][t|T].[n|N][a|A][m|M][e|E]. (.*)')

searchable = '''
    First Name: Jennifer Last Name: Johnson
    first name: Natalie last name: Robinson
    First-name- John Last-name- Ferguson
    first Name= Samuel last Name= Patterson
    First.Name: Jasmine Last.Name: James
    first.name: Patricia last.name: Hamilton
    First Name: Michael Last Name: Hensley
    Elijah Fisher
    Justin Wright
    Paula Reyes
'''

print(nameRegex.findall(searchable))

dotAllRegex = re.compile(r'.*', re.DOTALL)
