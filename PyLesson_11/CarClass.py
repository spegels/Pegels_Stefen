class Car:
    def __init__(self, p=0, i=0, e=0, t=0):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setCustom(self, pnt, ntrr, engn, trs):
        self.paint = pnt
        self.interior = ntrr
        self.engine = engn
        self.tires = trs

    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    paint = input("Enter paint color(red/black/silver): ")
    interior = input("Enter interior material(black leather/brown leather): ")
    engine = input("Enter engine specs(5/6/7 liter, v6/v8, 500-800hp): ")
    tires = input("enter tire type(road/sport): ")

    car1 = Car(paint, interior, engine, tires)

    print("Your Vehicle: ")
    print("Paint:    ",car1.getPaint())
    print("Interior:    ",car1.getInterior())
    print("Engine:    ",car1.getEngine())
    print("Tires:    ",car1.getTires())
main()

