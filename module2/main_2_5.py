talent = 20
pound = 32
lots = 13.3

talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
total_grams = (talent * talents + pounds) * pound * lots
kilogram = total_grams // 1000
gram = total_grams % 1000


print(f"The weight in modern units: {kilogram} kilograms and {gram} grams.")
