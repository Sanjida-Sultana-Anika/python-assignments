airport_info = {}

while True:
    user_input = int(input("To enter new airport press 1:\n"
                           "To fetch information of an existing airport press 2:\n"
                           "To quit press 3: "))

    if user_input == 1:
        icao_code = input("Enter ICAO code of airport: ")
        airport_name = input("Enter name of the airport: ")
        airport_info.update({icao_code: airport_name})
        print(f"Airport {icao_code} added to the database.")
    elif user_input == 2:
        icao_code = input("Enter ICAO code that you want to fetch: ")
        if icao_code in airport_info:
            print(f"The airport is {airport_info[icao_code]}")
        else:
            print("No information found.")
    elif user_input == 3:
        print("Goodbye.")
        break
    else:
        print("Invalid choice. You must choose 1/ 2/ 3.")
