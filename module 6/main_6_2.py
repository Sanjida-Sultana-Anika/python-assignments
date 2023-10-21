import random


def roll_dice(side_number):
    return random.randint(1, side_number)


userInput = int(input("Enter the number of side in your dice: "))
num_rolls = 0
while True:
    result = roll_dice(userInput)
    num_rolls += 1
    print(f"Roll {num_rolls}: {result}")
    if result == userInput:
        break

print(f"It took {num_rolls} rolls to get a {userInput}.")
