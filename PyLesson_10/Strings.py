go = input("Enter string: ")

splist = go.split(" ")


wordslist = []

spot = 0

for i in range(0,4):
    output = ""
    wordslist.append([])
    for j in range(0,4):
        wordslist[i].append(splist[spot])
        output += str(wordslist[i][j]) + "\t"
        if len(splist) > spot:
            spot +=1
    print(output + "\n")
