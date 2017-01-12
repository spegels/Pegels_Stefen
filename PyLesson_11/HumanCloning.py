class Human:
    def __init__(self, hair=0, eyes=0, skin=0):
        self.h = hair
        self.e = eyes
        self.s = skin


    def setHes(self, hare, Is, sccin):
        self.h = hare
        self.e = Is
        self.s = sccin


    def getHair(self):
        return self.h

    def getEyes(self):
        return self.e

    def getSkin(self):
        return self.s

def main():
    h = input("Enter hair color: ")
    e = input("Enter eye color: ")
    s = input("Enter skin color: ")


    human1 = Human(h, e, s)

    print("Your Human is ready: ")
    print("Info: ")
    print("Hair:    ",human1.getHair())
    print("Eyes:    ",human1.getEyes())
    print("Skin:    ",human1.getSkin())

    human1.setHes("brown", "blue", "gray")

    print("Example clone: ")
    print("Hair:    ",human1.getHair())
    print("Eyes:    ",human1.getEyes())
    print("Skin:    ",human1.getSkin())
    
main()
