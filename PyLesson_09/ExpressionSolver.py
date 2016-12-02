exp = input("Enter expression, with spaces between characters: ")
i = 0
eq = exp.split(" ")


while i < len(eq):
    if i < len(eq) and (eq[i] == "*" or eq[i] == "/"):
        if eq[i] == "*":
            eq[i] = int(eq[i-1]) * int(eq[i+1])
        else:
            eq[i] = (int(eq[i-1]) / int(eq[i+1]))
        eq.pop(i-1)
        eq.pop(i)
    else:
        i +=1

    
j = 0

while j < len(eq):
    if j < len(eq) and (eq[j] == "+" or eq[j] == "-"):
        if eq[j] == "+":
            eq[j] = (int(eq[j-1]) + int(eq[j+1]))
        else:
            eq[j] = (int(eq[j-1]) - int(eq[j+1]))
        eq.pop(j-1)
        eq.pop(j)
    else: 
        j +=1
        



print(eq)
