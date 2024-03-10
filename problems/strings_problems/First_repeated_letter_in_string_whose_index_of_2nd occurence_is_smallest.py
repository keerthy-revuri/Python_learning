#Given a string, find the first repeated character in it. We need to find the character that occurs more
#than once and whose index of second occurrence is smallest.
# here it is e as 2nd occurence index of e is less than 2nd occurence of g

def repeat(str):
    temp = {}
    for i in str:
        if i in temp:
            temp[i] = temp[i] + 1
            return i
        else:
            temp[i] = 1
    return "no repeated element"


res = repeat("geeksforgeeks")
print(res)