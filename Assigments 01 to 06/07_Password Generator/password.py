import random

print("Welcome to My Password Generator")
print('='*50)
print("This program generates a random password for you.")
print('='*50)

# Using a string instead of a set
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,;0123456789'

length = int(input("Enter the length of the password: "))
number = int(input('Amount of Passwords to generate: '))

print('\nHere are your Passwords: ')
print('='*50)
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)

print('='*50)
print('\nThank you for using my password generator!')
print('='*50)
print('Have a great day!')
print('='*50)
