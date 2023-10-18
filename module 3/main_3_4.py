year = int(input("Please enter your year:"))

if year % 4 == 0:
    print("Yay! It's a leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print("Wow! It's a leap year.")
else:
    print("Your year is a not a leap year")
