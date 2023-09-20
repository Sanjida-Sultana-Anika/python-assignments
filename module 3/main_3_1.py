size = int(input("Enter size of Zander in centimeters:"))

if size >= 42:
    print("Good catch mate!")
else:
    print("Please release the fish into the lake!")
    print(f"Your fish is", 42 - size, "cm short than the required size.")
