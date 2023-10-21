import random

number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10. Guess the number: ")

guess = int(input())

while guess != number:
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    guess = int(input())

print('Now you got the correct number!')
