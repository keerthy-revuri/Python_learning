
#Given a string, find the repeated character present first in the string


def repeat(str):

    a1 = []
    for i in str:
        a1.append(i)
    for i in range(len(a1)):
        if a1[i] in a1[i+1:]:
            return a1[i]
    return "no character is repeated"


res = repeat("hello")
print(res)

# logic 2

str = "geeksforgeeks"
temp = {}
for i in str:
    if i in temp:
        temp[i] = temp[i] + 1
    else:
        temp[i] = 1
print(temp)
for i in str:
     if temp[i] > 1:
         print(i)
         break


#logic 3 using lists
# for i in range(len(str)):
#      for j in range(i + 1, len(str)):
#          if str[i] == str[j]:
#              print(str[i])
#              break
#      break







