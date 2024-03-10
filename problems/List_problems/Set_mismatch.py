# set mismatch

#logic 2 using missing =  (sum of n numbers) - (sum of nums_set), duplicate = (sum of nums) - (sum of nums_set)

def findErrorNums(nums):
    n = len(nums)
    num_set = set(nums)

    duplicate = sum(nums) - sum(num_set)
    missing = (n * (n + 1) // 2) - sum(num_set)

    return [duplicate, missing]

nums = [1,2,4,4,5]
print(findErrorNums(nums))  # Output: [4, 3]


#logic 3 - using mathematical formula -
# assume ex - [1,2,2,4] substract from actual sequence - [1,2,3,4] (in this problem this is i)- from this if we substract each respective number from 2 lists we get 2-3 = -1, 2**2 - 3**2 = -5
# Duplicate - Missing = -1 ~ D-M = -1 , D**2 - M**2 = -5, if we solve this we get M = 3, from that D = 2
#So, lets assume D -M = X, D**2 - M**2 = Y, if we solve this we get M = (Y - X**2)/ 2X

def setmismatch(nums):
    n = len(nums)
    x = 0 # duplicate - missing
    y = 0 # duplicate**2 - missing**2

    for i in range(1 , n+1): # range is till N+1 as we are starting from 1
        x = x +nums[i-1] - i # if we just write x = nums[i-1] - i , then value will overridden every time, at last in this example it will be 4 - 4 = 0, instead of 2-3 = -1, so we add x = x + nums[i-1] - i
        y = y + nums[i-1]**2 -i**2

    missing = (y - x**2)// (2 * x)
    duplicate = missing + x
    return [duplicate, missing]

nums = [2,4,4,6]
res = setmismatch(nums)
print(res)


