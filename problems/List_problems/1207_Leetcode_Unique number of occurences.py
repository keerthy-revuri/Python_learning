def unique(arr):
    dict = {}
    a = []
    for num in arr:
        if num in dict:
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1
    print(f"dictionary is {dict}")
    for value in dict.values():
        a.append(value)
    print(f"list is {a}")
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            flag = False
            break
        else:
            flag = True
    return flag
arr = [1,2,1,1,2,3]
res = unique(arr)
print(res)