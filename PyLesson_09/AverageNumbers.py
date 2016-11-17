import random
nums = [1,2,3,4,5,6,7,8,9,10]
print("Numbers: ")
for i in range(0,10):
    nums.append(random.randint(1,100))
print(nums[10:len(nums)])
