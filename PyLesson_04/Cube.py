side=float(input("Enter the length of one side of the cube:"))
sa=6*side**2
def calcsurf(sa):
    sa=float("{:.5f}".format(sa))
    return(sa)
    
    
print("The surface are of a cube with side length",side,"is",calcsurf(sa))

