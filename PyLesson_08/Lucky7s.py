num = int(input("Enter number: "))

def luck(num):
    if num > 0:
        if (num % 10) == 7:
            num = int(num / 10)
            return int(1 + luck(num))
        else:
            num = int(num / 10)
            return int(0 + luck(num))
    else:
        return 0

print(luck(num))
