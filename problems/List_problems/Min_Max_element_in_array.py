#min max
def min_max(arr):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]

    max = arr[0]
    for j in range(len(arr)):
        if max < arr[j]:
            max = arr[j]

    return min, max

arr = [1,3,4,2,6,0]
res = min_max(arr)
print(f"minimum , maximum elements are {res}")
