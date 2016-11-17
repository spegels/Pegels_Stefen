mylist = ["cuttlefish","shrimp","squid","clam","barnacle"]
print("In order: ")
output = ""
output2 = ""

def reverse(output2):
    for i in range(len(mylist), 0 , -1):
        output2 += mylist[i - 1] + " "
    return output2

for i in mylist:
    output += i + " "
print(output)
print(" ")
print("Reversed: ")


print(reverse(output2))
        
    
