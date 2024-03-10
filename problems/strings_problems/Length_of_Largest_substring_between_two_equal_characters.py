#largest substring between 2 equal characters

def largest_substr(str):
    char_index = {}
    res = -1
    for i,char in enumerate(str):
        if char in char_index:
            res = max(res, i - char_index[char] -1)

        else:
            char_index[char] = i
    return res

str = 'abcagb'
res = largest_substr(str)
print(res)


#logic 2

str = 'abcajkha'
i_list = []
for i in range(len(str)):
    for j in range(i+1,len(str)):
        print(f" str[{i}] - {str[i]},str[{j}] is {str[j]}")
        if str[i] == str[j]:
            n = j - i - 1
            i_list.append(n)
            print(f"n is {n}")
print(max(i_list))
