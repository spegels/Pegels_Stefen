import random

class obj():
    def __init__(self, itemName, manufacturer, itemCategory = "", itemPrice = ""):
        self.item = itemName
        self.manuf = manufacturer
        self.cat = itemCategory
        self.price = itemPrice
        self.UPC = random.randint(1000000000,9999999999)

    def __str__(self):
        return "Item Info... \nItem Name: " + self.item + \
               "\nManufacturer: " +self.manuf + \
               "\nCategory: " + self.cat + \
               "\nPrice: " + self.price + \
               "\nUPC: " + str(self.UPC)

def main():
    item = input("Enter item name: ")
    manuf = input("Enter item manufacturer: ")

    catnprice = input("Will you enter category and price information?(y or n)")

    if catnprice == "n":
        item1 = obj(item, manuf)
    elif catnprice == "y":

        cat = input("Enter category: ")
        price = input("Enter price: ")
        item1 = obj(item, manuf, cat, price)
    else:
        print("Unknown command... ")
        main()

    print(item1.__str__())

main()
