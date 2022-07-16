import random

# Introduction
print("Welcome to Genemerator")
print("The last password generator you'll ever need")

# Password character's database
chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890`-=!@#$%^&*()_+[]\{}|;'':"",./<>?'

# Asking the amount of password needed to be generated
number = input("How many password(s) do you want me to generate-")
number = int(number)

# Asking password length
if(number==1):
    length = input("How long should the password be (20 Recommended)-")
else:
    length = input("How long should the passwords be (20 Recommended)-")
length = int(length)

# Printing the passwords
if(number==1):
    print("\nHere is your password-")
else:
    print("\nHere are your passwords-")

# Adding the base code of password generator
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

# About the author
print("Made by Aarush Chaudhary")
print("GitHub- LASTSECRET987")
print("https://github.com/LASTSECRET987/")