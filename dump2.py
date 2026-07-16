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


options()
