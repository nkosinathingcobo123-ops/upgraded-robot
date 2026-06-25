import csv

"""with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f'{row['Role']}')
"""


def cr(usernm):
    with open('users.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'.strip()] == usernm:
                return row
        return False


cr2 = cr('NgcoboManager')
if cr2:
    print(cr2['Password'.strip()])
    print(cr2['Role'])
