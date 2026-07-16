import csv

"""with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f'{row['Role']}')
"""


def cr(usernm):
    with open('userswithroles.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'.strip()] == usernm:
                return row
        return False


# Getting the roles of the users
cr2 = cr('NgcoboManager')
if cr2:
    print(cr2['Role'])


def abd(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


abd2 = abd(123456789)
print(abd2)
