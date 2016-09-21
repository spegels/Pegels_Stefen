def receipt(food, price):
    print("{:.<15}{:.>15.2f}".format(food,price))

food1=input("Please enter item 1:")
price1=float(input("Please enter the price of item 1:"))


food2=input("Please enter item 2:")
price2=float(input("Please enter the price of item 2:"))


food3=input("Please enter item 3:")
price3=float(input("Please enter the price of item 3:"))

food4="Subtotal:"
price4=price1+price2+price3

food5="Tax:"
price5=float((price1+price2+price3)/12.5)

food6="Total:"
price6=price1+price2+price3+price5



print("<<<<<<<<<<<<<<<<Receipt>>>>>>>>>>>>>>>")
receipt(food1, price1)
receipt(food2, price2)
receipt(food3, price3)
receipt(food4, price4)
receipt(food5, price5)
receipt(food6, price6)

print("____________________________________")
print("*Thank you for your support*")



