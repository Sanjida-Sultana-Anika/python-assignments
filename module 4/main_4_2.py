size = float(input("Insert your number in inches")) * 2.54

while size == size:
    if size < 0:
        break

    print(f"Here is your result in cm:", size)
   
    size = input("Insert your number in inches")
print("Don't put negative number")
