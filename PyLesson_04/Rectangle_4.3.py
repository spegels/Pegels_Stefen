l=float(input("Enter length of rectangle in feet:"))
w=float(input("Enter width of recangle in feet:"))
def calcPerim():
    global p
    p=float("{:.5f}".format(2*l+2*w))
def prnt():
    print("Your rectangle is",p,"ft around.")
calcPerim()
prnt()



