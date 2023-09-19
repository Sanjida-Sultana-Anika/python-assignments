#Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

import math

length = float(input("What's the length?:"))
width = float(input("What's the width?:"))
area = float(length * width)
print(f"Here is the area:", area)
perimeter = float(2 * (length + width))
print(f"Here is the perimeter:", perimeter)

