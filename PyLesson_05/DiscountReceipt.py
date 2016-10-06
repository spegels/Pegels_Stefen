item1=input("Please enter item 1:")
price1=float(input("Please enter the price of item 1:"))
item2=input("Please enter item 2:")
price2=float(input("Please enter the price of item 2:"))
item3=input("Please enter item 3:")
price3=float(input("Please enter the price of item 3:"))
item4=input("Please enter item 4:")
price4=float(input("Please enter the price of item 4:"))

subtotal=price1+price2+price3+price4

def discount():
    if subtotal >= 2000:
        discount = subtotal*0.15
    if subtotal < 2000:
        discount = subtotal*0
    print(discount)

def format(item,price):
    print("{:.<10}{:.>10}".format(item,price))

print("<<<<<<<<<<<<<<<Receipt>>>>>>>>>>>>>>>")
format(item1,price1)
format(item2,price2)
format(item3,price3)
format(item4,price4)
format("subtotal",subtotal)
format("discount",discount())
print("_____________________________________")
print("Thank you for shopping with us today.")

