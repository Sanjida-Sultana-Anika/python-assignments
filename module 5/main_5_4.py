cities = []

for i in range(5):
    userInput = input(f"Enter a city name: {i+1}. ")
    cities.append(userInput)

print("Cities in your list are:")
for city in cities:
    # city_per_line = city.split()
    print(city)
