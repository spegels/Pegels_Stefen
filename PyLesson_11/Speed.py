class MilesPerHour:
    def __init__(self, distance=0, hours=0, minutes=0):
        self.d = int(distance)
        self.hr = int(hours)
        self.mmin = int(minutes)
        mph = 0

    def sset(self, dst, hrs, mins):
        self.d = dst
        self.hr = hrs
        self.mmin = mins
        mph = 0

    def getHours(self):
        return self.hr

    def getMins(self):
        return self.mmin

    def getDistance(self):
        return self.d

    def getMph(self):
        mph = self.d / (self.hr + self.mmin / 60.0)
        return mph
        
def main():
    d = input("Enter distance, in miles: ")
    hr = input("Enter time, in hours: ")
    mmin = input("Enter time, in minutes: ")

    mph1 = MilesPerHour(d , hr, mmin)

    print("<<<<<<<<<<RESULTS>>>>>>>>>>")
    print(mph1.getDistance(),"miles in", mph1.getHours(),"hours = {:<.3f}".format(mph1.getMph()), "mph.")

    mph1.sset(10,2,25)

    print("<<<<<<<<<<RESULTS>>>>>>>>>>")
    print(mph1.getDistance(),"miles in", mph1.getHours(),"hours = {:<.3f}".format(mph1.getMph()), "mph.")

    
main()




    
    
    
