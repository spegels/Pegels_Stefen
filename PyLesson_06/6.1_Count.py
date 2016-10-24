first = int(input("Enter first number: "))
last = int(input("Enter final number to count up to: "))

output = " "
for i in range(first, (last+first), first):
    output = output + str(i) + " "

print(output)
