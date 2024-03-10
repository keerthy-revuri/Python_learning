def getMin(arr, n):
    #print(arr,n)
    if n==1:
        return arr[0]
    return min(arr[n-1], getMin(arr, n-1))


arr = [12,1234,45,67,1]
n = len(arr)
minimum = getMin(arr,n)
print(f"minimum element is {minimum}")

def getMax(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], getMax(arr, n-1))
arr = [12, 1234, 45, 67, 1]
n = len(arr)
maximum = getMax(arr,n)
print(f"maximum element is {maximum}")


