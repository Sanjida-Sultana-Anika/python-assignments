import random


def roll_dice():
    return random.randint(1, 6)


if __name__ == "__main__":
    num_rolls = 0
    while True:
        result = roll_dice()
        num_rolls += 1
        print(f"Roll {num_rolls}: {result}")
        if result == 6:
            break
        print(f"It took {num_rolls} rolls to get a 6.")
