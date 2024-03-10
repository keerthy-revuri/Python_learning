# using the existing array
#note - 2 main steps 1. divide the list until length is 1 (use recursion as the process is same
# 2. Conquer - merge the sorted lists using while loop,
# ammend the smallest in 2 sorted list to new sorted list (
#(or use same list but different index - k) and  move the index
#conquer - to be precise elements will be cmpared in 2 sorted lists, whichever is smaller it will be
#added to new list and its index will be increased
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        mergesort(L)
        R = arr[mid:]
        mergesort(R)
        i = j = k= 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1

arr = [5,8,12,56,7,9,45,51]

print(f"Given input is - {arr}")
mergesort(arr)
print(f"Sorted list is - {arr}")


# same logic using another list for storing sorted list

def mergesort(n):
    if len(n) > 1:
        mid = len(n)//2
        L = n[:mid]
        mergesort(L)
        R = n[mid:]
        mergesort(R)
        c = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                c.append(L[i])
                print(f"i is - {i}, c is - {c}")
                i = i + 1
            else:
                c.append(R[j])
                print(f"j is - {j}, c is - {c}")
                j = j + 1
        while i < len(L):
            c.append(L[i])
            i = i + 1
            print(f"separate while , i value - {i}, c - {c}")
        while j < len(R):
            c.append(R[j])
            j = j + 1
            print(f"separate while , j value - {j}, c - {c}")

    return c
n = [5,8,12,56,7,9,45,51]
res = mergesort(n)
print(f"final - {res}")
