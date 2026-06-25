"""..."""
import os
import string
import time
import random
import csv
import sys

# This is a sample Python script.

# Corect code


def generate_password(length=random.randint(8, 20)):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for j in range(length))


def cr(usernm):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'.strip()] == usernm:
                return True

        return False


usernamed = input('enter')
print(cr(usernamed))
generated_password = generate_password()
print(f'Generated password: {generated_password}')


def countd(sec):
    while sec >= 0:
        print(f'\r{sec} seconds remaining', end='', flush=True)
        time.sleep(1)
        sec -= 1


with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


def check_username_exists(username):
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'] == username:
                True
                print(f"Username '{username}' existssss.")
    False
    print(f"Username '{username}' does not existtttt.")


def check_passwordz(password, username):
    if check_username_exists(username) == True:
        with open('users.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f'checking password for username: {username}')
            for row in reader:
                if row['Password'] == password:
                    True
                    print(f"Password '{password}' existsssss.")
        False
        print(f"Password '{password}' does not existtttt.")


username = input("Enter your username: ")
password = input("Enter your password: ")
check_username_exists(username)
check_passwordz(password, username)


def check_password_exists(username, password):
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'] == username:
                True
                print(f"Username '{username}' exists.")
                if row['Password'] == password:
                    True
                    print(f"Password '{password}' exists.")
                else:
                    False
                    print(f"Password '{password}' does not exist.")
            else:
                False
                print(f"Username '{username}' does not exist.")

    False
    return f"Password '{password}' does not exist."


# check_password_exists('NgcoboAdmin', 'NgcoboAdmin123')

print('hijbm')


def check_password(password):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Password'] == password:
                True
                return f"Password '{password}' is correct."
    False
    return f"Password '{password}' is incorrect."


def choice1_of_1():
    print("You selected to login as a returning user.")
    print("Select these options below to proceed:\n\tPress 1 if you are fully registered and want to login.\n\tPress to if you are a new user who wants to finish registering.\n\tPress 3 if you want to exit the program.")
    selection = input("Enter your selection: ")
    if selection == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print(cpj(username))


def menu(choice):
    while True:
        if choice in ['1', '2', '3']:
            if choice == '1':
                print("You selected to login as a returning user.")
                print("Please enter your username and password to login.")
                username = input("Enter your username: ")
                print(cpj(username))
            elif choice == '2':
                print("Registering a new user.")
                username = input("Enter your username: ")
                message = cpj(username)
                print(message)
            elif choice == '3':
                print("Exiting the program. Goodbye!")
                sys.exit()
    else:
        print("Invalid choice. Please try again.")


def cpj(username):
    checking = check_username_exists(username)
    print(checking)
    if checking == True:
        password_entry = input("Enter your password: ")
        print(check_password_exists(password_entry))

        return f"Username '{password_entry}' exists."
    return f"Password does not exist."


abcj = cpj('NgcoboAdmin')
print(abcj)


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
    
        return True"""


def options():
    while True:
        print("Welcome to the Ngcobo login system.\nSelect 1 if you are a returning user.\nSelect 2 if you are a new user and want to register.\nSelect 3 if you want to exit the program.")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3']:
            return choice
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please try again.")


# print("Welcome to the Ngcobo login system.\nSelect 1 if you are a returning user.\nSelect 2 if you are a new user and want to register.\nSelect 3 if you want to exit the program.")
# choice = input("Enter your choice: ")
print(options())

menu(options())
choice = options()
menu(choice)  # message = cpj(username)
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
