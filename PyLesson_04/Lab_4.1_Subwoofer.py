def main(volume):
    return(height*width*length)
height=int(input("Please enter the height of the box, in inches:"))
width=int(input("Please enter the width of the box, in inches:"))
length=int(input("Please enter the length of the box, in inches:"))
volume=height*width*length
def calcvol(volumefeet):
    volumefeet="{:^10.2f}".format(volumefeet)
    return(volumefeet)
volumefeet= volume*0.00057870
print("The volume of your box is",calcvol(volumefeet),"cubic feet.")

