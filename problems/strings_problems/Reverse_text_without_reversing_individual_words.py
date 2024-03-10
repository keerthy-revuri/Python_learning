# logic 1
str1 = "geeks quiz practice code"
str2 = ''
list =[]
#for i in range(len(str1)):
       # list.append(str1[i])
list = str1.split(' ')
list.reverse()
str2 = ' '.join(list)
print(str2)


#logic 2

str = "i love to code"

temp = []
temp_1 = []
temp = str.split(' ')
print(temp)
for i in temp:
    print(i[::-1])
    temp_1.append(i[::-1])
print(temp_1)
str = ' '.join(temp_1)
print(str[::-1])