# Two pointers inplace solution using single loop
# i pointer is used for traversing array, j is a pointer used as index for tracking index of non- zero elements

nums = [2,0,1,3,0,8]
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j],nums[i] = nums[i], nums[j]

        print(f"nums[i] - {nums[i]}" )
        print(f"nums[j] - {nums[j]}")
        j = j + 1
print(nums)


#logic - using 2 pointers using 2 loops

nums = [2,0,1,3,0,8]
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j = j + 1
while j < len(nums):
    nums[j] = 0
    j = j + 1
print(nums)