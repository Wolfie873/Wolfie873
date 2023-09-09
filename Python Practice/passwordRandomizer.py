#python3
import random
import string

def generate_password(name, website, num_numbers):
    # Replace vowels in the name with numbers
    name = name.lower()
    name = name.replace('a', '4')
    name = name.replace('e', '3')
    name = name.replace('i', '1')
    name = name.replace('o', '0')
    name = name.replace('u', '9')
    website = website.lower()
    website = website.replace('a', '4')
    website = website.replace('e', '3')
    website = website.replace('i', '1')
    website = website.replace('o', '0')
    website = website.replace('u', '9')

    # Generate random numbers based on num_numbers
    random_numbers = ''.join(random.choice(string.digits) for _ in range(num_numbers))

    # Combine website, modified name, and random numbers to form the password
    password = website + '@' + name + random_numbers

    return password

print("What is your name or initials? (letters only)")
name = input()
if not name.isalpha():
    print("Invalid input. Name must contain only letters.")
    exit()

print("What website is the password for?")
website = input()

print("How many random numbers at the end? (numbers only)")
num_numbers = input()
if not num_numbers.isdigit():
    print("Invalid input. Please enter a valid number.")
    exit()

password = generate_password(name, website, int(num_numbers))
print("Generated password:", password)