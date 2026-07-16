
import csv
import secrets
import string
from pathlib import Path


USERS_FILE = Path(__file__).with_name("userswithroles.csv")
FIELDNAMES = ["Username", "Password", "Role"]


def normalize_user(row):
    return {
        "Username": (row.get("Username") or "").strip(),
        "Password": row.get("Password") or "",
        "Role": (row.get("Role") or "User").strip() or "User",
    }


def read_users():
    if not USERS_FILE.exists():
        return []

    with USERS_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [
            normalize_user(row)
            for row in reader
            if (row.get("Username") or "").strip()
        ]


def write_users(users):
    with USERS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(users)


def find_user(username):
    username = username.strip()
    for user in read_users():
        if user["Username"] == username:
            return user
    return None


def check_username_exists(username):
    return find_user(username) is not None


def authenticate_user(username, password):
    user = find_user(username)
    if user and user["Password"] == password:
        return user
    return None


def check_password_exists(username, password):
    return authenticate_user(username, password) is not None


def check_password(password):
    return any(user["Password"] == password for user in read_users())


def cr(username):
    return check_username_exists(username)


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."
    if not any(char.isalpha() for char in password):
        return False, "Password must contain at least one letter."
    return True, "Password is valid."


def login_user():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")
    user = authenticate_user(username, password)

    if user:
        print(f"Welcome, {user['Username']}! Role: {user['Role']}")
        return True

    if check_username_exists(username):
        print("Incorrect password.")
    else:
        print(f"Username '{username}' does not exist.")
    return False


def register_user():

    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return False
    if check_username_exists(username):
        print(f"Username '{username}' already exists.")
        return False

    while True:
        password = input("Choose a password, or press Enter to generate one: ")
        if not password:
            password = generate_password()
            print(f"Generated password: {password}")
            break

        is_valid, message = validate_password(password)
        if is_valid:
            break
        print(message)

    role = input("Role [User]: ").strip() or "User"
    users = read_users()
    users.append({"Username": username, "Password": password, "Role": role})
    write_users(users)
    print(f"User '{username}' registered as {role}.")
    return True


def options():
    while True:
        print("\nWelcome to the Ngcobo login system.")
        print("1. Login as a returning user")
        print("2. Register a new user")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


def menu():
    while True:
        choice = options()

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        else:
            print("Goodbye!")
            break


def main():
    menu()


if __name__ == "__main__":
    main()
