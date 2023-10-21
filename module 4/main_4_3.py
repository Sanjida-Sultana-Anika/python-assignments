largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    try:
        num_float = float(num)
        if largest is None or num_float > largest:
            largest = num_float
        if smallest is None or num_float < smallest:
            smallest = num_float
    except ValueError:
        print("Invalid input.")

if largest is not None:
    print(f"Maximum is {largest}.")
if smallest is not None:
    print(f"Minimum is {smallest}.")
