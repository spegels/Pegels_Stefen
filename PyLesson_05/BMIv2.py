h1 = int(input("Please enter your height, in inches:"))
w1 = int(input("Please enter your weight, in pounds:"))
bmi = 0

def calcBMI(h,w):
    global bmi
    bmi = (w*703)/(h**2)
    if bmi > 39.9:
        cond = 6
    elif bmi >= 35:
        cond = 5        
    elif bmi >= 29.9:
        cond = 4        
    elif bmi >= 25:
        cond = 3        
    elif bmi >= 18.5:
        cond = 2        
    elif bmi < 18.5:
        cond = 1

calcBMI(h1, w1)
        
def calcCond(condition):
    if cond == 6:
        print("Condition is morbidly obese")
    if cond == 5:
        print("Condition is very obese")
    if cond == 4:
        print("Condition is obese")
    if cond == 3:
        print("Condition is overweight")
    if cond == 2:
        print("Condition is healthy")
    if cond == 1:
        print("Condition is underweight")
    
    


print("Your bmi is:",bmi)

print(
