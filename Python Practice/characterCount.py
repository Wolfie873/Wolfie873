message = 'It was a cold day in June and before I continue let me stop.'
msg = input()
count = {} # Something like 'r' is the key and it counts how many r there are

for character in msg:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)