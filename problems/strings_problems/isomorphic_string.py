
#logic 1
str1 = 'abc'
str2 = 'xzyd'
if len(str1) == len(str2):

    temp1 = { }
    for i in str1:
        if i in temp1:
            temp1[i] = temp1[i] + 1
        else:
            temp1[i] = 1
    print(temp1)

    temp2 = { }
    for i in str2:
        if i in temp2:
            temp2[i] = temp2[i] + 1
        else:
            temp2[i] = 1
    print(temp2)

    temp3 = { }
    for i in range(len(str1)):
        if str1[i] not in temp3:
            temp3[str1[i]] = str2[i]
    print(temp3)
    tmp = True
    for i in temp3:

        if temp1[i] == temp2[temp3[i]]:
             tmp = True
        else:
            tmp = False
            break
    if tmp == True:
        print(f"{str1} and {str2} are isomorphic")
    else:
        print(f"{str1} and {str2} are not isomorphic")

else:
    print("not isomorphic")