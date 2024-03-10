
def Redistribute(words):
    str = ''.join(words)
    n = len(str)
    #print(n)
    dict = {}
    for i in str:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    #print(dict)

    for char, value in dict.items():
        if n % value != 0:
            return False

    return True

words = ["aabc", "aabc", "bc"]
res = Redistribute(words)
print(res)