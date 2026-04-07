users = {}

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        users[username] = password

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if users.get(username) == password:
            print("Login successful")
        else:
            print("Invalid credentials")

    elif choice == "3":
        break
