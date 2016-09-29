l=float(input("Enter length of rectangle in feet:"))
w=float(input("Enter width of recangle in feet:"))
p=2*l+2*w
def calcPerim(p):
    p=float("{:.5f}".format(p))
    return(p)
    
print("Your rectangle is",calcPerim(p),"sq ft around.")

