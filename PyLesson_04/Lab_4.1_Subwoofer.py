def main(volume):
    return(height*width*length)
height=float(input("Please enter the height of the box, in inches:"))
width=float(input("Please enter the width of the box, in inches:"))
length=float(input("Please enter the length of the box, in inches:"))
volume=height*width*length
def calcvol(volumefeet):
    volumefeet=float("{:^10.5f}".format(volumefeet))
    return(volumefeet)
volumefeet= volume*0.00057870
print("The volume of your box is",calcvol(volumefeet),"cubic feet.")

