import math


def unit_price_pizza(diameter, price):
    radius = diameter / 2
    area_cm_square = math.pi * (radius ** 2)
    area_meter_square = area_cm_square / 10000
    unit_price = price / area_meter_square
    return unit_price


diameter1 = float(input("Enter diameter for pizza 1 (in cm):"))
price1 = float(input("Enter price for pizza 1 (in euro):"))
unit_price1 = unit_price_pizza(diameter1, price1)

diameter2 = float(input("Enter diameter for pizza 2 (in cm):"))
price2 = float(input("Enter price for pizza 2 (in euro):"))
unit_price2 = unit_price_pizza(diameter2, price2)

print(f"Unit price of pizza 1 is {unit_price1:.2f}.")
print(f"Unit price of pizza 2 is {unit_price2:.2f}.")

if unit_price1 < unit_price2:
    print("Pizza 1 is giving better value for money. Buy Pizza 1.")
elif unit_price1 > unit_price2:
    print("Pizza 2 is giving better value for money. Buy Pizza 2.")
else:
    print("Both pizzas have the same unit price.")
