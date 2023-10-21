names = set()

while True:
    user_input_name = input("Enter a name or press enter: ")
    if user_input_name == "":
        break

    if user_input_name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(user_input_name)
for name in names:
    print(name)
