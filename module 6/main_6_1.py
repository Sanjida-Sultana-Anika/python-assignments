import random


def roll_dice():
    return random.randint(1, 6)


def main():
    num_rolls = 0
    result = None
    while True:
        result = roll_dice()
        num_rolls += 1
        print(f"Roll {num_rolls}: {result}")
        if result == 6:
            break
    print(f"It took {num_rolls} rolls to get a 6.")


main()
