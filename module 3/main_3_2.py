print("Welcome to the cruise ship! We provide LUX, A, B, and C cabin classes.")
cabinClass = input("Please select your cabin class: ").upper()
cabin1 = "LUX"
cabin2 = "A"
cabin3 = "B"
cabin4 = "C"

if cabinClass == cabin1:
    print("LUX: upper-deck cabin with balcony.")
elif cabinClass == cabin2:
    print("A: above the car deck, equipped with a window.")
elif cabinClass == cabin3:
    print("B: windowless cabin above the car deck.")
elif cabinClass == cabin4:
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
