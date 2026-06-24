"""..."""
import os
import string
import time
import random
import csv
import sys

# This is a sample Python script.
chars = string.ascii_letters + string.digits + string.punctuation
# print('hello world')
password = ''.join(random.choice(chars) for i in range(12))
username = ''.join(random.choice(string.ascii_lowercase +
                   string.digits) for i in range(8))
# method to countdown from a given number of seconds

print(f'Your generated username is: {username}')
print(f'Your generated password is: {password}')


def countd(sec):
    while sec >= 0:
        print(f'\r{sec} seconds remaining', end='', flush=True)
        time.sleep(1)
        sec -= 1


with open('users.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


def check_username(username):
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'] == username:
                return True
    return False


def check_password(password):
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Password'] == password:
                return True
    return False


def menu(choice):
    if choice == '1':
        print("You selected to login again")
        print("Please enter your username and password to login.")
        username = input("Enter your username: ")
        print(cpj(username))
    elif choice == '2':
        print('duh')
    elif choice == '3':
        print("You selected to check if a user has created a password.")
        username = input("Enter your username: ")
        message = cpj(username)
        print(message)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")


def cpj(username):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'.strip()] == username:
                if row['Password'.strip()]:
                    print('Enter your password to login.')
                    password = input("Enter your password: ")
                    if row['Password'.strip()] == password:
                        check_password(password)
                        return 'Login successful.'
                return 'Password does not exist.'
        return 'Username does not exist.'


def validate_password(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False


"""if len(password) < 8:
        return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password):
            return False
        return True"""


def options():
    print("Welcome to the Ngcobo login system.\nSelect 1 if you are a returning user.\nSelect 2 if you are a new user and want to register.\nSelect 3 if you want to exit the program.")
    choice = input("Enter your choice: ")
    if choice not in ['1', '2', '3']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please try again.")
        return options()
    return choice


# print("Welcome to the Ngcobo login system.\nSelect 1 if you are a returning user.\nSelect 2 if you are a new user and want to register.\nSelect 3 if you want to exit the program.")
# choice = input("Enter your choice: ")
print(options())

menu(options())
# username = input("Enter a username to check: ")
# password = input("Enter the password: ")
# print(check_username(username))
# message = cpj(username)
print('nhghhhggfvtrggvtggvrf')
# print(message)


"""if check_username(username):
    print("Username exists.")
    password = input("Enter the password: ")

else:
    print("Username does not exist.")"""

"""def countdown(seconds):
if
    
    while seconds >= 0:
        os.system('cls')
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time up!")
countdown(5)
inp = int(input("Enter a number of seconds to countdown: "))
countdown(inp)
for i in range(5, -1, -1):
    os.system('cls')
    print(i)
    time.sleep(1)
print("Time's up!")
"""


countd(5)
