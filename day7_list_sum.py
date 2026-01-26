numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("Numbers:", numbers)
print("Sum:", sum(numbers))