#Given an integer array nums, return true if any value appears at least twice in the array,
#and return false if every element is distinct.
def repeat(num):

    for i in range(len(num)):
        if num[i] in num[i+1:]:
            return True
        else:
            return False

res = repeat([1,2,3,1])
print(res)
