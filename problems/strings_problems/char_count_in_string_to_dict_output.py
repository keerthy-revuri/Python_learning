#Count the frequency of characters in a string and move it to dictionary

str1 = 'aaab'
temp = { }
for i in str1:
    if i in temp:
        temp[i] = temp[i] + 1
    else:
        temp[i] = 1
print(temp)


str1 = 'xxyy'
temp = { }
for i in str1:
    if i not in temp:
        c1 = str1.count(i)
        temp[i] = c1
print(temp)