talents = float(input("Enter talents: ")) * 20 * 32 * 13.3
pounds = float(input("Enter pounds: ")) * 32 * 13.3
lots = float(input("Enter lots: ")) * 13.3

total_grams = talents + pounds + lots
kilogram = total_grams // 1000
gram = round(total_grams % 1000, 2)

print(f"The weight in modern units: {kilogram:.2f} kilograms and {gram:.2f} grams.")
