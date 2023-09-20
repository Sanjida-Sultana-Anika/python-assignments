import random

three_digit_code = [random.randint(0, 9) for _ in range(3)]
four_digit_code = [random.randint(1, 6) for _ in range(4)]

print("Random 3-digit code:", three_digit_code)
print("Random 4-digit code:", four_digit_code)
