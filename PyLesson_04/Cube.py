side=float(input("Enter the length of one side of the cube:"))
sa=6*side**2
def calcsurf():
    sa=float("{:.5f}".format(6*side**2))
    return(sa)
def prnt():
    print("The surface are of a cube with side length",side,"is",sa)

calcsurf()
prnt()
    


