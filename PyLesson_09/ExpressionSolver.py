exp = input("Enter expression, with spaces between characters: ")
i = 0
eq = exp.split(" ")


while i < len(eq):
    if i < len(eq) and (eq[i] == "*" or eq[i] == "/"):
        if eq[i] == "*":
            eq[i] = (int(eq[i-1]) * int(eq[i+1]))
        else:
            eq[i] = (int(eq[i-1]) / int(eq[i+1]))
        eq.pop(i-1)
        eq.pop(i)
    i +=1

    


while i < len(eq):
    if i < len(eq) and (eq[i] == "+" or eq[i] == "-"):
        if eq[i] == "+":
            eq[i] = (int(eq[i-1]) + int(equ[i+1]))
        else:
            eq[i] = (int(eq[i-1]) - int(equ[i+1]))
        eq.pop(i-1)
        eq.pop(i)
    i +=1



print(eq)
