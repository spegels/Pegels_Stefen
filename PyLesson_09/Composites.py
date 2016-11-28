nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]
def gfactor():
    for i in nums:
        global nums
        if i % (nums.index(i) + 1) == 0:
            return 1
        else:
            return 0
        

def remcomp():
    for i in nums:
        if gfactor() == 0:
            nums.remove(nums[i])
    return nums

remcomp()
print(nums)
