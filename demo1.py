"""..."""
import os
import time
import csv

# This is a sample Python script.

# print('hello world')

# method to countdown from a given number of seconds


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
        password = input("Enter your password: ")
        cpj(username)
    else:
        print("Invalid choice. Please try again.")


choice = input("Enter your choice (1 to login again): ")


def cpj(username):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'.strip()] == username:
                if row['Password'.strip()]:
                    return 'Password exists.'
                return 'Password does not exist.'
        return 'Username does not exist.'


username = input("Enter a username to check: ")
# password = input("Enter the password: ")
print(check_username(username))
message = cpj(username)
print('nhghhhggfvtrggvtggvrf')
print(message)

menu(choice)

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


def countd(sec):
    while sec >= 0:
        print(f'\r{sec} seconds remaining', end='', flush=True)
        time.sleep(1)
        sec -= 1


countd(5)
