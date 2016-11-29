nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]

def gfactor(num):
    for i in range(2,num-1,1):
        if num % i == 0:
            return 1
    return 0
        

def remprimes(lst):
    start = 0
    for i in range(0,len(lst),1):
        if gfactor(lst[start]) == 0:
            lst.pop(start)
        elif start < len(lst):
            start +=1
    print(lst)


remprimes(nums)



