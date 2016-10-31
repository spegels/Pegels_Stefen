number = int(input("Enter integer: "))
digits = 0
average = 0

def avDigits(digits, average):
    num = number
    while num > 0:
        digits += 1
        average = average + (num % 10)        
        num = int(num / 10)
    average = average / digits    
    return average

print("The average of the digits in" , number, "is", avDigits(digits, average))
