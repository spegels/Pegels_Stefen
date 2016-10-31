number = int(input("Enter integer value: "))
num = number
rev = 0

def getReverse(num, rev):
    while num > 0:
        rev = rev*10
        rev = rev + (num % 10)
        num = int(num / 10)
    return rev

print(number, "reversed is" ,getReverse(num, rev))
