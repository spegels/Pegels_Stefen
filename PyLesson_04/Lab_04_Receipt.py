def receipt(food, price):
    print("{:.<15}{:.>15.2f}".format(food,price))

food1=input("Please enter item 1:")
price1=float(input("Please enter the price of item 1:"))


food2=input("Please enter item 2:")
price2=float(input("Please enter the price of item 2:"))


food3=input("Please enter item 3:")
price3=float(input("Please enter the price of item 3:"))



print("<<<<<<<<<<<<<<<<Receipt>>>>>>>>>>>>>>>")
receipt(food1, price1)
receipt(food2, price2)
receipt(food3, price3)

print("{:.<15}{:.>15.2f}".format("Subtotal:",price1+price2+price3))

TaxTotal=(price1+price2+price3)/10
print("{:.<15}{:.>15.2f}".format("Tax:", TaxTotal))

Sale=price1+price2+price3+TaxTotal
print("{:.<15}{:.>15.2f}".format("Total:",Sale))

print("____________________________________")
print("*Thank you for your support*")

