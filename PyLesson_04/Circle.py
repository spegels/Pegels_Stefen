r=float(input("Enter value of circle's radius:"))
area=2*3.14*r
def circArea():
    area=float("{:.5f}".format(2*3.14*r))
    return(area)
def prnt():
    print("The area of a circle with radius",r,"is",area)

circArea()
prnt()



