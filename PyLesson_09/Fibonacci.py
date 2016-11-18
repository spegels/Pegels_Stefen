start = int(input("Please enter your starting number: "))
size = int(input("Please enter sequence size: "))

seq = []

for i in range(0,size):
    if i<=1:
        seq.append(start)
    else:
        x = seq[i-1] + seq[i-2]
        seq.append(x)

print(seq)

