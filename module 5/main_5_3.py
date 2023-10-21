userInput = int(input("Enter your number: "))

prime = True

if userInput <= 1:
    prime = False
else:
    for i in range(2, userInput):
        if userInput % i == 0:
            prime = False
            break

if prime:
    print("Yes, the number is prime.")
else:
    print("No, the number is not prime.")
