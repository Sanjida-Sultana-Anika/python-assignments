seasons = ("spring", "summer", "autumn", "winter")
month = int(input("Enter any number from 1 to 12: "))

if month == 12 or month == 1 or month == 2:
    print("Oh it's the winter season!")
elif month == 3 or month == 4 or month == 5:
    print("Oh it's the spring season!")
elif month == 6 or month == 7 or month == 8:
    print("Oh it's the summer season!")
elif month == 9 or month == 10 or month == 11:
    print("Oh it's the autumn season!")
else:
    print("Invalid input. Please enter a number from 1 to 12")
