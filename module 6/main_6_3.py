def convert_gasoline_gallon(gallons):
    return gallons * 3.78541


def main():
    while True:
        gallon_to_litre = input("Enter the quantity of gasoline in American gallons (or a negative value to exit):")

        gallons = float(gallon_to_litre)

        if gallons >= 0:
            liters = convert_gasoline_gallon(gallons)
            print(f"{gallons} gallons is equal to {liters} liters.")
        else:
            print("Exiting the program.")
            break


main()
