def binary(a,low,high,x):
    while low <= high:
        #print(f"low value is - {low}")
        #print(f"high value is - {high}")
        mid = low + (high-low)//2
        #print(f"mid value is - {mid}")
        if a[mid] == x:
            return mid
           # print(f"mid value when both are equal - {mid}")
        elif a[mid] < x:

            low = mid + 1
            #print(f"low value is - {mid + 1}")
        else :
            high = mid - 1
    return -1

a = [2,3,5,6,7,9]
x = 5
low = 0
#print(f"low value is - {low}")
high = len(a)-1

res = binary(a,low,high,x)
print(res)