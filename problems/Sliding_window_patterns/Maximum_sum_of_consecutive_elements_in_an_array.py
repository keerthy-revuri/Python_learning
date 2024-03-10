#maximum sum of consecutive k elements

#logic1 - using sliding window

def max_of_k_consecutive(nums,k):
     n = len(nums)
     if n < k:
         return "size of k is more than array size"
     max_sum = sum(nums[:k])
     window_sum = max_sum
     for i in range(k,n):
         window_sum = window_sum + nums[i] - nums[i-k]
         max_sum = max(window_sum, max_sum)
     return max_sum

nums = [100,200,300,400]
k = 2
res = max_of_k_consecutive(nums,k)
print(f"maximum sum of {k} consecutive elements is {res}")


# logic2 - using bruteforce

def max_of_k_consecutive(nums,k):
    n = len(nums)
    sum_1 = 0
    maximum = float('-inf')
    for i in range(n-k+1):
        sum_1 = sum(nums[i:i+k])

        # if sum > max:
        #     max = sum
        maximum = max(sum_1, maximum)
    return maximum
nums = [100,200,300,400]
k = 2
res = max_of_k_consecutive(nums,k)
print(res)
