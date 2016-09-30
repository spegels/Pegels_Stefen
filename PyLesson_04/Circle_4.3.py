r=float(input("Enter value of circle's radius:"))

def circArea():
    global area
    area=float("{:.5f}".format(2*3.14*r))
def prnt():
    print("The area of a circle with radius",r,"is",area)
circArea()
prnt()

