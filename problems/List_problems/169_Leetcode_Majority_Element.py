# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Input: nums = [3,2,3]
# Output: 3
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#logic 1 - convert list to dictionary with occurence as value, compare values againt half length of array
nums = [2,2,1,1,1,2,2]
i_dict = { }
n = len(nums)
for i in nums:
    if i in i_dict:
        i_dict[i] = i_dict[i] + 1
    else:
        i_dict[i] = 1
for i in i_dict:
    if i_dict[i] > n // 2:
        print(i)
print(i_dict)





