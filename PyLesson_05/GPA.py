g1 = input("Please enter letter grade for class 1:")
g2 = input("Please enter letter grade for class 2:")
g3 = input("Please enter letter grade for class 3:")
g4 = input("Please enter letter grade for class 4:")
g5 = input("Please enter letter grade for class 5:")
g6 = input("Please enter letter grade for class 6:")
g7 = input("Please enter letter grade for class 7:")

def calcPoints(g): 
    if g == "a":
        g = float(4)       
    elif g == "b":
        g = float(3)
    elif g == "c":
        g = float(2)
    elif g == "d":
        g = float(1)
    elif g == "f":
        g = float(0)
    return g



def calcGPA():
    global GPA
    GPA = float((calcPoints(g1) + calcPoints(g2) + calcPoints(g3) + calcPoints(g4) + calcPoints(g5) + calcPoints(g6) + calcPoints(g7))/7)



calcGPA()
print("Your GPA  is {:1.1f}".format(GPA))
