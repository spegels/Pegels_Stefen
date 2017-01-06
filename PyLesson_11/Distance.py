import math


class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.xOne = int(x1)
        self.yOne = int(y1)
        self.xTwo = int(x2)
        self.yTwo = int(y2)

    def reset(self, newx1, newy1, newx2, newy2):
        self.xOne = newx1
        self.yOne = newy1
        self.xTwo = newx2
        self.yTwo = newy2

    def getDist(self):
        d = math.sqrt((self.xTwo - self.xOne)*(self.xTwo - self.xOne) + (self.yTwo - self.yOne)*(self.yTwo - self.yOne));
        return d


def main():
    x1 = input("Enter first x-coordinate: ")
    y1 = input("Enter first y-coordinate: ")
    x2 = input("Enter second x-coordinate: ")
    y2 = input("Enter second y-coordinate: ")

    d1 = Distance(x1, y1, x2, y2)

    print("Distance = {:<.3f}".format(d1.getDist()))

    d1.reset(0,0,2,2)

    print("Distance = {:<.3f}".format(d1.getDist()))

main()



    
    
    
