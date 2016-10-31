number = int(input("Enter integer value: "))
sum = 0
num = number

def sumDigits(num,sum):
    while num > 0:
        sum = sum + (num % 10)
        num = int(num / 10)
    return sum


print("The sum of the digits in", number, "is", sumDigits(num,sum))
