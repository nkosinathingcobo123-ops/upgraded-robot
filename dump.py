
import random
import time
import csv
import string

input_tries = 5


def check_username_exists(username):
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Username'] == username:
                True
                print(f"Username '{username}' exist.")
            else:
                False
                print(f"Username '{username}' does not exis*.")


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


with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

username = input("Enter your username: ")
password = input("Enter your password: ")

# check_passwordz(password, username)

with open('users.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


def cr(usernm):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'.strip()] == usernm:
                return True
        return False


print(cr(username))


def password_available(password):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Password'].strip() == password:
                True
                return f'Password "{password}" is correct.'
        False
        return f"Password '{password}' is incorrect."


def check_password_exists(username):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        if cr(username) == True:
            print(f'Username "{username}" exists.')
            password = input("Enter your password: ")
            for row in reader:
                if row['Password'].strip() == password:
                    True
                    return f'Password "{password}" is correct.'
            False
            return f"Password '{password}' is incorrect."
        else:
            return f"Username '{username}' does not exist."


def generate_password(length=random.randint(8, 20)):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for j in range(length))


generated_password = generate_password()
print(f'Generated password: {generated_password}')


def countd(sec):
    while sec >= 0:
        print(f'\r{sec} seconds remaining', end='', flush=True)
        time.sleep(1)
        sec -= 1


def incorrect_password(username):
    with open('users.csv', 'r', encoding='utf-8'):
        if check_password_exists(username) == False:
            print('dud')


# print(password_available(password))
# print(cr(username))
# print(check_username_exists(username))
print(check_password_exists(username))
