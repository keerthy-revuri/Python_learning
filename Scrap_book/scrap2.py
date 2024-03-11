def merge_two_sorted(arr1, arr2):
    arr3 = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr3.append( arr1[i])
            i = i + 1
        else:
            arr3.append( arr2[j])
            j = j + 1
    while i < len(arr1):
        arr3.append(arr1[i])
        i = i + 1
    while j < len(arr2):
        arr3.append(arr2[j])
        j = j + 1
    return arr3

arr1 = [1,2,4]
arr2 = [1,3,4]
res = merge_two_sorted(arr1, arr2)
print(res)
