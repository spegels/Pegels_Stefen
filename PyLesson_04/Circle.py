r=float(input("Enter value of circle's radius:"))

def circArea():
    area=float("{:.5f}".format(2*3.14*r))
    return(area)
def prnt():
    print("The area of a circle with radius",r,"is",area)
area=2*3.14*r

circArea()
prnt()



