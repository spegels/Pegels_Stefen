r=float(input("Enter value of circle's radius:"))
area=2*3.14*r
def circArea(area):
    area=float("{:.5f}".format(area))
    return(area)

print("The area of a circle with radius",r,"is",circArea(area))
