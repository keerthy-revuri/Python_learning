#Given an integer array nums, return true if any value appears at least twice in the array,
#and return false if every element is distinct.
def repeat(num):
    temp={}
    lis=[]
    for i in num:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    print(temp)
    lis = []
    for i in temp:
        if temp[i] > 1:
            lis.append(i)
    print(lis)

res = repeat([1,2,3,6,8,2,1])
print(res)
