#outer loop - for min position
# inner loop - swapping
# It is a simple algorithm , it works by simply selecting smallest or largest element from unsorted portion of the array
# and swapping it with sorted portion of the array

list = [2,3,8,2,7,5, 5]
for i in range(len(list)):
    minpos = i
    for j in range(i,len(list)):
        if list[j] < list[minpos]:
            minpos = j

    temp = list[i]
    list[i] = list[minpos]
    list[minpos] = temp

print(list)


#Note - find the minimum index using the inner loop for the whole iteration, and then swap