gender = input("Select biological gender 'male/ female': ")
hemoglobin = float(input("Please type your hemoglobin value:"))

gender1 = "female"
gender2 = "male"

if gender == gender1 and 117 <= hemoglobin <= 155:
    print("Your hemoglobin level is normal")
elif gender == gender1 and hemoglobin < 117:
    print("Oh gosh, your hemoglobin level is low!")
elif gender == gender1 and hemoglobin > 155:
    print("Oh my! You have high level of hemoglobin.")

elif gender == gender2 and 134 <= hemoglobin <= 167:
    print("Your hemoglobin level is normal")
elif gender == gender2 and hemoglobin < 134:
    print("Oh gosh, your hemoglobin level is low!")
elif gender == gender2 and hemoglobin > 167:
    print("Oh my! You have high level of hemoglobin.")
else:
    print("Invalid input.")
