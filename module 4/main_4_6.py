import random

number = int(input("Enter a number: "))
points_inside_circle = 0
total_points = 0

while total_points < number:
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    if x**2 + y**2 < 1:
        points_inside_circle += 1
    total_points += 1

approx_pi = 4 * points_inside_circle / total_points
print(f"Approx of pi: {approx_pi:.2f}")
