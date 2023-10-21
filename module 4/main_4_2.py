while True:
    size = float(input("Insert your number in inches: ")) * 2.54
    if size < 0:
        print("Don't put negative number")
        break
    else:
        print(f"Here is your result in cm: {size:.2f}")
