str = "geeks for geeks"
for i in range(len(str)):
    if str[i] in str[i+1:]:
        print(str[i])
        break