numbers = []

while True:
    var = input("Enter number: ")
    if var == "":
        break
    else:
        numbers.append(int(var))

numbers.sort(reverse=True)

loopCount = 5
if len(numbers) < 5:
    loopCount = len(numbers)

for i in range(loopCount):
    print(f"Number {i+1}: {numbers[i]}")

