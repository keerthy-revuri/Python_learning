# maximum product of 2 elements in an array
# find max, second max elements and find product of both
def max_product_of_two_elements(arr):
    if len(arr) < 2:
        return "cannot find product if array size is less than 2"

    # Initialize the maximum and second maximum
    max1 = float('-inf')
    max2 = float('-inf')

    # Iterate through the array
    for num in arr:
        if num > max1:
            # If the current number is greater than max1, update max1 and shift max1 to max2
            max2 = max1
            max1 = num
        elif num > max2:
            print("else if")
            # If the current number is greater than max2 but not max1, update max2
            max2 = num

        print(f" max1: {max1}")
        print(f" max2: {max2}")

    # Return the product of the two maximum elements
    return max1 * max2


# Example usage:
arr = [1, 6, 3, 4, 5]
print(max_product_of_two_elements(arr))  # Output: 20 (5 * 4)



#logic2 - use sort() , then find product of last 2, if -ve numbers are present -
# find maximum product of first 2 or last2 elements

# use sort()
def max_product_using_sorting(nums):
    if len(nums)< 2:
        return "product is not posiible"
    nums.sort()
    print(nums)
    return max(nums[0]*nums[1], nums[-1]*nums[-2])

nums = [-9,1,6,4,3,7,-10]
res = max_product_using_sorting(nums)
print(f" maximum product is {res}")



#logic3 - using brute force method using 2 for loops


def maximum_product(nums):
    product = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # print(nums[i], nums[j])
            if product < ((nums[i] - 1) * (nums[j] - 1)):
                product = ((nums[i] - 1) * (nums[j] - 1))
            # print((nums[i]-1) * (nums[j] - 1))
    return product
nums = [2,3,4,5,6,7]
res = maximum_product(nums)
print(res)