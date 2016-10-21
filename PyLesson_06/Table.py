num = int(input("Enter number: "))
size = int(input("Enter number of table rows: "))

for i in range(1, size+1):
    print("{:2.0f}    {:2.0f}".format(i, i*num))
