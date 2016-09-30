l=float(input("Enter length of rectangle in feet:"))
w=float(input("Enter width of recangle in feet:"))
p=2*l+2*w
def calcPerim():
    p=float("{:.5f}".format(2*l+2*w))
    return(p)
def prnt():
    print("Your rectangle is",p,"sq ft around.")
calcPerim()
prnt()


