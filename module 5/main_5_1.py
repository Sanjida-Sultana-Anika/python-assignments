import random

roll = int(input("How many dice to roll?:"))
sum_of_numbers = 0

for i in range(roll):
    number = random.randint(1, 6)
    sum_of_numbers += number

print(sum_of_numbers)
