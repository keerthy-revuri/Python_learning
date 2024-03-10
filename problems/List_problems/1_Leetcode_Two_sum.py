# Given an array of integers nums and a integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9 , Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#logic 3 - using dictionaries

def two_sum(nums, target):
    for i in range(n):
        diff = target - nums[i]
        if diff in i_dict:
            return [i_dict[diff] , i]
        else:
            i_dict[nums[i]] = i
nums = [2,11,7,15]
target = 9
n = len(nums)
i_dict = {}
result = two_sum(nums, target)
print(result)


#logic 1

nums = [2,11,7,15]
target = 9
n = len(nums)
i_list = []
for i in range(n):
    for j in range(i, n):
        #
        if i not in i_list:
            if nums[i] + nums[j] == target:
                i_list.append(i)
                i_list.append(j)
                print(f"after every iteration - {i,j}")
print(i_list)

#logic 2 - using 1 for loop

nums = [1,11,10,15]
target = 11
n = len(nums)
i_list =[]
for i in range(n):
    if target - nums[i] in nums:
        i_list.append(i)
print(i_list)







