#! python3
import pprint

message = 'It was a cold day in June and before I continue let me stop.' # The triple quote ''' can be used for inserting multiple lines of text
msg = input()
count = {} # Something like 'r' is the key and it counts how many r there are

for character in msg.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)