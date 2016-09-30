num1=float(input("Enter value 1:"))
num2=float(input("Enter value 2:"))
num3=float(input("Enter value 3:"))
avg=(num1+num2+num3)/3
def average():
    avg=float("{:.5f}".format((num1+num2+num3)/3))
    return(avg)
def prnt():
    print("The average of",num1,num2,"and",num3,"is",avg)

average()
prnt()


