num = int(input("Enter number: "))

factorial = 1

for i in range(1, num):
    factorial = factorial + factorial*i

print(factorial)
