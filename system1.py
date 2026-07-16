import csv
import time
import os
import sys


def clear_line():
    """Clear the current line"""
    sys.stdout.write('\r')
    sys.stdout.write(' ' * 50)
    sys.stdout.write('\r')
    sys.stdout.flush()


def load_users():
    """Load users from CSV file"""
    users = {}
    try:
        with open('user.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row['Username']] = {
                    'Password': row['Password'],
                    'Role': row['Role']
                }
    except FileNotFoundError:
        print("Users file not found. Creating sample file...")
        create_sample_file()
        return load_users()
    return users


def create_sample_file():
    """Create a sample users.csv file"""
    with open('user.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Password', 'Role'])
        writer.writerow(['admin', 'admin123', 'Administrator'])
        writer.writerow(['john', 'pass123', 'User'])
        writer.writerow(['jane', 'jane456', 'Manager'])
        writer.writerow(['bob', 'bob789', 'Developer'])
    print("Sample users.csv file created successfully!")


def countdown_timer(seconds):
    """Display countdown timer that updates in place"""
    print("Please wait: ", end='')
    for i in range(seconds, 0, -1):
        sys.stdout.write(f'{i} seconds')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\r' + ' ' * 30 + '\r')
        # sys.stdout.write('Please wait: ')
        sys.stdout.flush()
    print("\nYou can try again now!\n")
    clear_line()  # Clear the line after countdown is complete


def countd(sec):
    while sec >= 0:
        print(f'\r{sec} seconds remaining', end='', flush=True)
        time.sleep(1)
        sec -= 1


def count_down(sec):
    for remaining in range(sec, 0, -1):
        sys.stdout.write(f"\r{remaining} seconds remaining")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.flush()


count_down(10)


def login(users, user_type):
    """Handle user login with 5 attempts"""
    print(f"\n{'='*40}")
    print(f"   {user_type} Login")
    print(f"{'='*40}")

    Username = input("Enter Username: ")

    if Username not in users:
        print("❌ Username not found!")
        input("\nPress Enter to continue...")
        return False

    attempts = 5

    while attempts > 0:
        Password = input(
            f"Enter Password ({attempts} attempt{'s' if attempts > 1 else ''} remaining): ")

        if Password == users[Username]['Password']:
            print(f"\n{'='*40}")
            print(f"✓ Welcome {users[Username]['Role']} {Username}")
            print(f"{'='*40}\n")
            input("Press Enter to continue...")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(
                    f"❌ Incorrect Password! {attempts} attempt{'s' if attempts > 1 else ''} remaining.\n")
            else:
                print("\n" + "="*40)
                print("❌ TOO MANY FAILED ATTEMPTS!")
                print("="*40)
                countdown_timer(30)
                return False

    return False


def main():
    """Main function"""
    print("Loading users...")
    users = load_users()
    print(f"✓ {len(users)} users loaded successfully!\n")

    while True:
        # Clear screen (optional - comment out if you don't want this)
        # os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "="*40)
        print("       🔐 LOGIN SYSTEM 🔐")
        print("="*40)
        print("1. Returning User")
        print("2. In Progress User")
        print("3. Exit")
        print("="*40)

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            login(users, "RETURNING USER")
        elif choice == '2':
            login(users, "IN PROGRESS USER")
        elif choice == '3':
            print("\n" + "="*40)
            print("   Thank you! Goodbye! 👋")
            print("="*40 + "\n")
            break
        else:
            print("\n❌ Invalid option! Please select 1, 2, or 3.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
