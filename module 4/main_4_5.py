username = input("Enter username:")
password = input("Enter password:")

attempt = 0

while True:
    if username != 'python' or password != 'rules':
        if attempt >= 4:
            print("Access Denied")
            break
        print("Wrong, enter again:")
        username = input("Enter username:")
        password = input("Enter password:")
    elif username == 'python' and password == 'rules':
        print("Welcome.")
        break
    attempt += 1
