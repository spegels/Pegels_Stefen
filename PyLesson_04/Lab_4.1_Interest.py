def interest(amount):
    amount="${:<10.2f}".format(amount/(years*12))
    return(amount)


principle=float(input("Please enter your intial monetary value to be invested:"))

rate=float(input("Please enter the interest rate, as a decimal to be multiplied by 100%:"))

number=float(input("Please enter the number of times your loan is compounded per year:"))

years=float(input("Please enter the life of the loan(in years):"))

amount=principle*((1+(rate/number))**(number*years))
print("The total payment amount on your loan is:",interest(amount))
        
