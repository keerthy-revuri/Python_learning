elements = [16,2,5,8,0]
n = len(elements)
temp = elements[0]
elements[0] = elements[n-1]
elements[n-1] = temp
print(elements)


# print(n)
# for i in range(n):
#    for j in range(n-i-1):
#        if elements[j]>elements[j+1]:
#           tmp = elements[j]
#           elements[j] = elements[j+1]
#           elements[j+1] = tmp
#        print(elements)


for x in range(5):
 print(x)
