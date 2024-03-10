elements = [8,9,3,0,23]
n = len(elements) #length of array
for i in range(n): # pushes largest element to right most in every iteration, range is used when index of element is required ( in general to compare)
    for j in range(n-i-1): # this loop comapares adjacent elements in the array
        if elements[j] > elements[j+1]:
            temp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1] = temp
print(elements)



#Bubble sort using function
def sort(elements):
    n = len(elements)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
    return elements


elements = [4,8,3,2,9]
result = sort(elements)
print(result)


# bubble sort using main function
