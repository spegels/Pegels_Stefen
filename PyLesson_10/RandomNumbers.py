import random

numslist = []


for i in range(0,4):
    numslist.append([])
    for j in range(0,4):
        numslist[i].append(random.randint(1,100))

for nums in numslist:
    output = ""
    for num in nums:
        output += str(num) + "\t"
    print(output + "\n")
