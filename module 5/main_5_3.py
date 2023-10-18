userInput = int(input("Enter your number: "))

prime = True

for i in range(userInput):
    if i == 0 or i == 1:
        continue
    if userInput % i == 0:
        prime = False
        break

if prime:
    print("Yes, the number is prime.")
else:
    print("No, the number is not prime.")
