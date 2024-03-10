
def isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False

    temp1 = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 in temp1 and temp1[c1]!=c2:
            return False

        temp1[c1] = c2
    return True

result = isomorphic('xyxrr', 'zmzju')
print(result)