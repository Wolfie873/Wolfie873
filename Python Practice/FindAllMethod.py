#! python3
import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''Contact Info.
cel. 787-598-4920
jorge.ortiz20@outlook.com
phone. 909-876-6625
Canovanas, PR
abilify. (344) 234-3432134
        
Availability

 Full availability


Summary

Experienced sales consultant with a heavy history of customer service and problem solving skills. Proficient at handling tough clients and calming down agitated ones to create a space for communication and resolving issues. Through experiences in sales, communications and public relations I have learned how to treat clients as well as meeting their expectations for care and satisfaction. Am also very calm and collected, almost impossible to anger and don’t take critiques personally.
Education


B.A. Degree in Communications with a concentration on Public Relations – UPR Carolina
September 2009 - December 2016    
High School Diploma – Academia Del Carmen
2009
experience

Customer Care Rep | Alight Solutions | June 2019 - current

Description: As part of the payroll and garnishment department my job includes, dealing 
with tough customer and their payroll benefits. I must also create solutions for the client’s     employees and handle each call with care and understanding, as this directly affects the     employees lives and their well-being. Besides this I have been trained in Health and Welfare benefits and as such have learned to handle calls that include medical, dental and vision insurance as well as more extensive training on handling tough calls and questions from our customers.


T-mobile Telesales Rep | Linkactiv (787) 706-2910| November 2015 - May 2016

Description: Tasks included serving customers with an upbeat attitude, asking probing questions to determine customers needs and wants, and fit a plan and devices that would better suit the customer.


Apple Master Mobile/Sales Consultant | Best Buy (813) 558-7039 | October 2017 - December 2018

Description: Ask exploratory questions to customers and create rapport to find out their needs and use my knowledge of the product to offer the most complete solution for them. As an Apple Master I also had the task to have specialized knowledge on all Apple products and keep my customers and teammates informed on said products and train them on their use and unique value.


          Intern | Strategic Minds (787) 782-8300 | Junio 2013 – Noviembre 2013
Description: Prepare market and competitor analyses using various investigation tools in a tight timeframe. Also helped with the graphic design because of my advanced knowledge in the Adobe Creative Suite.

cualifications



Dedicated
Born Leader
Responsible
Fully Bilingual (Spanish and English)
Service Oriented
Trained in call center environment
Fast Learner
Creative Writer
Experience in analyzing markets
Hard Worker
Trained in selling techniques and strategies.
Imaginative
Resourceful
Work well with others
'''

print(phoneRegex.findall(resume))

digitRegex = re.compile(r'\d') # This is a 0-9 digit number
notdigitRegex = re.compile(r'\D') # This is not a 0-9 digit number
stringRegex = re.compile(r'\w') # This is the same as the word character
notstringRegex = re.compile(r'\W') # This is the same as the word character, includes underscore
spaceRegex = re.compile(r'\s') # This is the space character, includes tab and new line
notspaceRegex = re.compile(r'\S') # This is the space character, includes tab and new line

christmas = '''On the first day of Christmas, my true love sent to me
A partridge in a pear tree
On the second day of Christmas, my true love sent to me
2 turtledoves
And a partridge in a pear tree
On the third day of Christmas, my true love sent to me
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 4th day of Christmas, my true love sent to me
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the fifth day of Christmas, my true love sent to me
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 6th day of Christmas, my true love sent to me
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 7th day of Christmas, my true love sent to me
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 8h day of Christmas, my true love sent to me
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the ninth day of Christmas, my true love sent to me
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 10th day of Christmas, my true love sent to me
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the 11th day of Christmas, my true love sent to me
I sent 11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
On the twelfth day of Christmas, my true love sent to me
12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 gold rings (5 golden rings)
4 calling birds
3 French hens
2 turtledoves
And a partridge in a pear tree
And a partridge in a pear tree
'''

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall(christmas))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall("The brown cow makes vanilla icecream."))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall("The brown cow makes vanilla icecream."))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall("The brown cow makes vanilla icecream."))