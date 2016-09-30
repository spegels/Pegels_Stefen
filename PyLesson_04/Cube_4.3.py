side=float(input("Enter the length of one side of the cube:"))

def calcsurf():
    global sa
    sa=float("{:.5f}".format(6*side**2))
    
    
calcsurf()
print("The surface are of a cube with side length",side,"is",sa)
