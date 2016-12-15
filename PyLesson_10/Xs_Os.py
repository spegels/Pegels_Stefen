import random

xando = []

for i in range(0,4):
    xando.append([])
    for j in range(0,4):
        switch = random.randint(1,100)
        if switch == 1:
            xando[i].append("X")
        else:
            xando[i].append("O")
for values in xando:
    output = ""
    for value in values:
        output += str(value) + "\t"
    print(output + "\n")
